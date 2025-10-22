import { defineAuth } from '@aws-amplify/backend-auth';

export const auth = defineAuth({
  loginMechanisms: ['email'],    // or ['username'] / ['phone_number']
  allowGuestAccess: true,        // needed for public @auth rules
  externalProviders: []          // satisfies the CDK’s expectation
});