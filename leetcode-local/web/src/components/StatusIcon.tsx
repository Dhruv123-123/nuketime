import { Status } from '../api';

export default function StatusIcon({ status, size = 16 }: { status: Status; size?: number }) {
  if (status === 'solved') return <span title="Solved" style={{ color: 'var(--accent)', fontSize: size }}>✔</span>;
  if (status === 'attempted') return <span title="Attempted" style={{ color: 'var(--medium)', fontSize: size }}>◐</span>;
  return <span style={{ color: '#555', fontSize: size }}>○</span>;
}
