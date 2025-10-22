// Create a new voice memo record
export const createVoiceMemo = /* GraphQL */ `
  mutation CreateVoiceMemo($input: CreateVoiceMemoInput!) {
    createVoiceMemo(input: $input) {
      id
      timestamp
      audioKey
      latitude
      longitude
      transcript
    }
  }
`;