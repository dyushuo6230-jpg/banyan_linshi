import React, { useEffect, useMemo, useState } from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, useLocation, useNavigate } from 'react-router-dom';
import { Alert, App as AntApp, Button, Card, ConfigProvider, Descriptions, Form, Input, Space, Tag, Typography } from 'antd';
import { PageContainer, ProCard, ProLayout } from '@ant-design/pro-components';
import { api, type Json } from './api';
import './styles.css';

type Surface = { path: string; name: string; endpoint?: string; method?: 'GET' | 'POST' };
const surfaces: Surface[] = [
  { path: '/dashboard', name: 'Dashboard', endpoint: '/api/status' },
  { path: '/runtime-policy', name: 'Runtime / Policy', endpoint: '/api/policy' },
  { path: '/project-safety', name: 'Project Safety', endpoint: '/api/project-safety' },
  { path: '/gate-blockers', name: 'Gate / Blockers', endpoint: '/api/status' },
  { path: '/preflight', name: 'Preflight', endpoint: '/api/preflight', method: 'POST' },
  { path: '/commit-plan', name: 'Commit Plan', endpoint: '/api/commit/plan', method: 'POST' },
  { path: '/dry-run-result', name: 'Dry-run Result', endpoint: '/api/commit/dry-run', method: 'POST' },
  { path: '/trace-audit', name: 'Trace / Audit', endpoint: '/api/trace?offset=0&limit=50' },
  { path: '/provenance', name: 'Provenance', endpoint: '/api/provenance/UNKNOWN' },
  { path: '/provider-bindings', name: 'Provider Bindings', endpoint: '/api/providers' },
  { path: '/stage-run', name: 'Stage / Run', endpoint: '/api/stages?offset=0&limit=25' },
  { path: '/activation-readiness', name: 'Activation Readiness', endpoint: '/api/activation-readiness' },
];

function defaultBody(name: string): Json {
  if (name === 'Preflight') return { action_id: 'webui-preflight', action_type: 'inspect', precondition_results: {} };
  if (name === 'Commit Plan') return { classifications: {} };
  if (name === 'Dry-run Result') return { plan: { groups: [], classifications: {}, blocked_paths: [], leftovers: [] }, authorization_ref: null };
  return {};
}

function BanyanApp() {
  const navigate = useNavigate();
  const location = useLocation();
  const surface = useMemo(() => surfaces.find((item) => item.path === location.pathname) ?? surfaces[0], [location.pathname]);
  const [result, setResult] = useState<Json>({ state: 'READY' });
  const [error, setError] = useState<string>();

  const load = async () => {
    if (!surface.endpoint) return;
    setError(undefined);
    try {
      const method = surface.method ?? 'GET';
      setResult(await api(surface.endpoint, method === 'POST' ? { method, body: JSON.stringify(defaultBody(surface.name)) } : undefined));
    } catch (value) { setError(value instanceof Error ? value.message : String(value)); }
  };
  useEffect(() => { void load(); }, [surface.path]);

  return <ProLayout
    title="Banyan Control Plane"
    logo={<span className="banyan-mark">榕</span>}
    location={{ pathname: surface.path }}
    route={{ path: '/', routes: surfaces.map(({ path, name }) => ({ path, name })) }}
    menuItemRender={(item, dom) => <a onClick={() => navigate(item.path ?? '/dashboard')}>{dom}</a>}
    layout="mix" fixedHeader fixSiderbar
  >
    <PageContainer title={surface.name} subTitle="Runtime-backed · local-only · dry-run boundary">
      <Space direction="vertical" size="large" style={{ width: '100%' }}>
        <Alert type="info" showIcon message="The WebUI collects intent and renders typed Runtime results. It grants no authorization." />
        <ProCard title="Runtime result" extra={<Tag color="green">PRESERVED CONTRACT</Tag>}>
          {error ? <Alert type="error" message={error} /> : <pre data-testid="runtime-result">{JSON.stringify(result, null, 2)}</pre>}
        </ProCard>
        <Card title="Request boundary">
          <Descriptions column={1} size="small" items={[
            { key: 'route', label: 'Route', children: surface.endpoint },
            { key: 'authority', label: 'UI authority', children: 'NONE' },
            { key: 'mutation', label: 'Current project Git mutation', children: 'DISABLED' },
          ]}/>
          <Form layout="vertical"><Form.Item label="Intent note"><Input placeholder="Displayed locally; never treated as authorization" /></Form.Item></Form>
          <Button onClick={() => void load()}>Refresh typed result</Button>
        </Card>
      </Space>
    </PageContainer>
  </ProLayout>;
}

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode><ConfigProvider theme={{ token: { colorPrimary: '#176b52', borderRadius: 6 } }}><AntApp><BrowserRouter><BanyanApp /></BrowserRouter></AntApp></ConfigProvider></React.StrictMode>,
);
