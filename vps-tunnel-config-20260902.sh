#!/usr/bin/env bash
set -euo pipefail

source_env=/home/ubuntu/discord-mcp/secrets/tunnel.env
target_dir=/home/ubuntu/vps-le-comptoir/secrets
target_env="$target_dir/tunnel.env"
client=/home/ubuntu/tunnel-client/tunnel-client
profile=vps-le-comptoir
tunnel_id=tunnel_6a9880976db0819192eeae26f27b108e

[[ -r "$source_env" ]] || { echo "missing-source-env" >&2; exit 1; }
[[ -x "$client" ]] || { echo "missing-tunnel-client" >&2; exit 1; }

set -a
source "$source_env"
set +a
[[ -n "${CONTROL_PLANE_API_KEY:-}" ]] || { echo "missing-runtime-key" >&2; exit 1; }

mcp_url="$(sudo bash /home/ubuntu/vps-le-comptoir/scripts/show-tunnel-url.sh)"
"$client" init --force --profile "$profile" --tunnel-id "$tunnel_id" --mcp-server-url "$mcp_url" >/dev/null

install -d -m 0700 "$target_dir"
umask 077
printf 'CONTROL_PLANE_API_KEY=%s\nCONTROL_PLANE_TUNNEL_ID=%s\n' "$CONTROL_PLANE_API_KEY" "$tunnel_id" >"$target_env"

sudo tee /etc/systemd/system/vps-le-comptoir-tunnel.service >/dev/null <<EOF
[Unit]
Description=OpenAI Tunnel - VPS Le Comptoir
After=network-online.target vps-le-comptoir-mcp.service
Wants=network-online.target
Requires=vps-le-comptoir-mcp.service

[Service]
Type=simple
User=ubuntu
EnvironmentFile=$target_env
ExecStart=$client run --profile $profile
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable --now vps-le-comptoir-tunnel.service
sleep 3
sudo systemctl is-active --quiet vps-le-comptoir-tunnel.service
"$client" doctor --profile "$profile" --explain >/dev/null
echo tunnel-ready
