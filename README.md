# M82 CORE-V6 — Sovereign Debt, Collateral, Carry & Oil Hedge Engine

Sistema automatizado de monitoreo macroeconómico, valuación de deuda soberana distressed, colateral corporativo, funding carry y cobertura energética con inmutabilidad SSOT en GitHub.

## Arquitectura del Ecosistema (6 Métricas CORE)

| Componente | Descripción | Fuente / Estándar |
| :--- | :--- | :--- |
| Daemon Loop | Monitoreo y despacho en segundo plano (ciclos de 5 min) | Python 3 / Termux |
| SSOT Engine | Firmado SHA-256 (64 caracteres) e inmutabilización en main | GitHub API v3 |
| Sovereign Debt | Marcaje Mark-to-Market (VEN 2027 50.60c / PDVSA 2020 50.70c) | TRACE / Bloomberg |
| Collateral Module | Valuación de PDVSA 2020 vinculada a subasta de Citgo ($13.0B EV) | Delaware Court Filings |
| Funding & Carry | Tasa SOFR 1M (4.32%) vs Yield VEN 2027 (+13.96% Net Carry) | FRED / Federal Reserve |
| Oil Hedge Module | Rastreo WTI (>$87) / Brent (~$92) como catalizador de recovery | LSEG / ICE Futures |

## Especificaciones de Seguridad & Audit-Trail

1. Firmado Forense: Digest SHA-256 completo de 64 caracteres por cada dossier JSON.
2. Log de Gobernanza: Registro inmutable almacenado en Governance/logs/audit.log y sincronizado en main.
3. OPSEC & Storage: Supresión de marcadores temporales explícitos en notificaciones y rotación diaria de logs en crontab.

*Propiedad Intelectual: M82 Sovereign Core / All Rights Reserved.*
