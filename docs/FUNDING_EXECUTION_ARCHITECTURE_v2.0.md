# AURELIS Funding Execution Architecture v2.0

## Цель

Превратить поиск финансирования из списка ссылок в воспроизводимый конвейер с доказательствами.

## Контуры

1. **Scout** — собирает только первичные источники.
2. **Verifier** — проверяет статус, дедлайн, условия и соответствие.
3. **Ranker** — ставит приоритет по fit/deadline/effort.
4. **Proposal Builder** — формирует технический пакет из уже существующих AURELIS артефактов.
5. **Submission Adapter** — отдельный адаптер на каждый внешний канал: GitHub PR, web-form, email.
6. **Settlement Verifier** — отдельно подтверждает award и фактическое поступление.
7. **Ledger** — неизменяемая локальная история переходов.

## Главное архитектурное правило

Внешний канал не является частью ядра AURELIS. Каждый канал — сменный адаптер. Поэтому отказ одного канала не останавливает весь конвейер.

## Текущие приоритеты

- AnySearch Open Source Bounty — максимальный приоритет.
- Tether Developer Grants — второй поток.
- ARIA Scaling Trust — третий поток.

## Статусы

DISCOVERED -> VERIFIED -> ELIGIBLE -> PROPOSED -> SUBMITTED -> AWARDED -> SETTLEMENT_VERIFY -> PAID

Переход в SUBMITTED допустим только при наличии внешнего идентификатора submission/PR/Claim ID.
Переход в PAID допустим только при независимом подтверждении расчёта.

## Безопасность

Никаких секретов в исходниках, журнале, prompt'ах и evidence bundle. Защищённое ядро AURELIS не публикуется. Публичный слой содержит только open-source компоненты.

## Исполнение

aurelis_open_core/funding_runner.py генерирует:
- funding_state/execution_plan.json
- funding_state/OPERATOR_QUEUE.md

Эти файлы являются машинно-читаемым состоянием и очередью действий, а не имитацией внешних отправок.
