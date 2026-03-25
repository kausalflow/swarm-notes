import fs from 'fs';
import { loadEnv } from 'vite';

// We can just dump the result of the loader inside Astro, 
// but it's easier to just modify index.astro to print the IDs to a file during build.
