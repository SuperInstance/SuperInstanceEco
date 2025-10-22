import { defineBackend } from '@aws-amplify/backend';
import { auth } from './auth/resource.js';
import { defineData } from '@aws-amplify/backend-data';

const backend = defineBackend({
  auth,
  data: defineData({
    schema: 'schema.graphql',
  }),
});

export default backend;