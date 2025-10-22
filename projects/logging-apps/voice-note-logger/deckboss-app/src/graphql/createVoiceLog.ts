import { gql } from 'graphql-tag';

export const createVoiceLog = gql`
  mutation CreateVoiceLog(
    $id: ID!
    $timestamp: AWSDateTime!
    $location: String
    $audioUrl: String
    $notes: String
  ) {
    createVoiceLog(
      id: $id
      timestamp: $timestamp
      location: $location
      audioUrl: $audioUrl
      notes: $notes
    ) {
      id
      timestamp
      location
      audioUrl
      notes
    }
  }
`;