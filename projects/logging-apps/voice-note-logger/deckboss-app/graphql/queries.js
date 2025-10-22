// List all voice memos
export const listVoiceMemos = /* GraphQL */ `
  query ListVoiceMemos {
    listVoiceMemos {
      items {
        id
        timestamp
        audioKey
        latitude
        longitude
        transcript
      }
    }
  }
`;