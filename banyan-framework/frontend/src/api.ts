export type Json = Record<string, unknown>;

export async function api(path: string, init?: RequestInit): Promise<Json> {
  const response = await fetch(path, {
    ...init,
    headers: { 'Content-Type': 'application/json', ...(init?.headers ?? {}) },
  });
  const value = await response.json() as Json;
  if (!response.ok) throw new Error(String(value.error ?? `HTTP_${response.status}`));
  return value;
}
