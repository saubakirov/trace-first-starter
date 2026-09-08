FROM python:3.13-slim

COPY sidecar_allowlist_probe.py /opt/tfw/sidecar_allowlist_probe.py
USER 65532:65532
ENTRYPOINT ["python", "/opt/tfw/sidecar_allowlist_probe.py"]
