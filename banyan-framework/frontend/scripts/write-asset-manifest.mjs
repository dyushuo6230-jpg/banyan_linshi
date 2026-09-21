import { createHash } from 'node:crypto';
import { readdir, readFile, writeFile } from 'node:fs/promises';
import { join, relative } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = fileURLToPath(new URL('../../control-plane-go/internal/webassets/dist/', import.meta.url));
async function files(dir) {
  const entries = await readdir(dir, { withFileTypes: true });
  return (await Promise.all(entries.map((entry) => entry.isDirectory() ? files(join(dir, entry.name)) : [join(dir, entry.name)]))).flat();
}
const rows = [];
for (const path of (await files(root)).sort()) {
  if (path.endsWith('asset-manifest.json')) continue;
  const data = await readFile(path);
  rows.push({ path: relative(root, path), sha256: createHash('sha256').update(data).digest('hex') });
}
await writeFile(join(root, 'asset-manifest.json'), JSON.stringify({ schema_version: 'stage18.5-v1', assets: rows }, null, 2) + '\n');
