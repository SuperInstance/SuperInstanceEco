import React, { useEffect, useState } from 'react';
import {
  View,
  Text,
  TextInput,
  Button,
  ScrollView,
  StyleSheet,
  TouchableOpacity,
} from 'react-native';
import { StatusBar } from 'expo-status-bar';
import * as Location from 'expo-location';
import { Amplify } from 'aws-amplify';
import amplifyConfig from './src/amplify_outputs.json';
import { generateClient } from 'aws-amplify/api';

Amplify.configure(amplifyConfig);

export default function App() {
  const [memos, setMemos] = useState([]);
  const [text, setText] = useState('');
  const [showTime, setShowTime] = useState(true);
  const [showGPS, setShowGPS] = useState(true);
  const client = generateClient();

  const fetchMemos = async () => {
    try {
      const result = await client.graphql({
        query: `
          query ListVoiceNotes {
            listVoiceNotes {
              items {
                id
                text
                timestamp
                latitude
                longitude
              }
            }
          }
        `,
      });
      setMemos(result.data.listVoiceNotes.items.reverse());
    } catch (err) {
      console.error('Error fetching memos:', err);
    }
  };

  const logMemo = async () => {
    try {
      const { status } = await Location.requestForegroundPermissionsAsync();
      if (status !== 'granted') return;

      const location = await Location.getCurrentPositionAsync({});
      const { latitude, longitude } = location.coords;

      const result = await client.graphql({
        query: `
          mutation CreateVoiceNote($input: CreateVoiceNoteInput!) {
            createVoiceNote(input: $input) {
              id
              text
              timestamp
              latitude
              longitude
            }
          }
        `,
        variables: {
          input: {
            id: `note-${Date.now()}`,
            text,
            timestamp: new Date().toISOString(),
            latitude,
            longitude,
          },
        },
      });

      setText('');
      fetchMemos();
    } catch (err) {
      console.error('Error logging memo:', err);
    }
  };

  useEffect(() => {
    fetchMemos();
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.header}>🧠 Capitaine AI Memo Stream</Text>

      <View style={styles.toggleRow}>
        <TouchableOpacity onPress={() => setShowTime(!showTime)}>
          <Text style={styles.toggle}>⏱️ {showTime ? 'Hide Time' : 'Show Time'}</Text>
        </TouchableOpacity>
        <TouchableOpacity onPress={() => setShowGPS(!showGPS)}>
          <Text style={styles.toggle}>📍 {showGPS ? 'Hide GPS' : 'Show GPS'}</Text>
        </TouchableOpacity>
      </View>

      <ScrollView style={styles.scroll}>
        {memos.map((memo) => (
          <View key={memo.id} style={styles.bubble}>
            <Text style={styles.memoText}>{memo.text}</Text>
            {showTime && <Text style={styles.meta}>🕒 {new Date(memo.timestamp).toLocaleString()}</Text>}
            {showGPS && (
              <Text style={styles.meta}>
                📍 {memo.latitude.toFixed(4)}, {memo.longitude.toFixed(4)}
              </Text>
            )}
          </View>
        ))}
      </ScrollView>

      <View style={styles.inputRow}>
        <TextInput
          style={styles.input}
          placeholder="Type a memo..."
          value={text}
          onChangeText={setText}
        />
        <Button title="Send" onPress={logMemo} />
      </View>

      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#eef',
    paddingTop: 40,
    paddingHorizontal: 10,
  },
  header: {
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 10,
    textAlign: 'center',
  },
  toggleRow: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    marginBottom: 10,
  },
  toggle: {
    fontSize: 14,
    color: '#007AFF',
  },
  scroll: {
    flex: 1,
    marginBottom: 10,
  },
  bubble: {
    backgroundColor: '#fff',
    padding: 10,
    marginVertical: 5,
    borderRadius: 10,
    alignSelf: 'flex-start',
    maxWidth: '80%',
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowRadius: 3,
    elevation: 2,
  },
  memoText: {
    fontSize: 16,
  },
  meta: {
    fontSize: 12,
    color: '#555',
    marginTop: 4,
  },
  inputRow: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 10,
  },
  input: {
    flex: 1,
    backgroundColor: '#fff',
    padding: 10,
    borderRadius: 8,
    marginRight: 10,
  },
});