import { generateClient } from 'aws-amplify/data';
import outputs from './amplify_outputs.json';

type VoiceNote = {
  id: string;
  timestamp: string;
  gps: string;
  note: string;
};

const client = generateClient<VoiceNote>({ outputs });

async function testCreateNote() {
  const result = await client.models.VoiceNote.create({
    timestamp: new Date().toISOString(),
    gps: '57.0516,-135.3300',
    note: 'Test note from Sitka!',
  });

  console.log('Created voice note:', result);
}

testCreateNote();