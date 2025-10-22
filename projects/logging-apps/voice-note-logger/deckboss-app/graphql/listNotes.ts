import { gql } from 'graphql-tag';

export const listNotes = gql`
  query ListNotes {
    listNotes {
      items {
        id
        content
        createdAt
      }
    }
  }
`;