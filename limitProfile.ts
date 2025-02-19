










export { createProfile };}  return saveProfile(profileData);  }    throw new Error('Já existe um perfil cadastrado.');  if (existingProfile) {  const existingProfile = await findProfile(); async function createProfile(profileData) {import { findProfile, saveProfile } from './profileService';