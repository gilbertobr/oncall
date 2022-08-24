class OrganizationLogType:
    (
        TYPE_SLACK_DEFAULT_CHANNEL_CHANGED,
        TYPE_SLACK_WORKSPACE_CONNECTED,
        TYPE_SLACK_WORKSPACE_DISCONNECTED,
        TYPE_TELEGRAM_DEFAULT_CHANNEL_CHANGED,
        TYPE_TELEGRAM_CHANNEL_CONNECTED,
        TYPE_TELEGRAM_CHANNEL_DISCONNECTED,
        TYPE_INTEGRATION_CREATED,
        TYPE_INTEGRATION_DELETED,
        TYPE_INTEGRATION_CHANGED,
        TYPE_HEARTBEAT_CREATED,
        TYPE_HEARTBEAT_CHANGED,
        TYPE_CHANNEL_FILTER_CREATED,
        TYPE_CHANNEL_FILTER_DELETED,
        TYPE_CHANNEL_FILTER_CHANGED,
        TYPE_ESCALATION_CHAIN_CREATED,
        TYPE_ESCALATION_CHAIN_DELETED,
        TYPE_ESCALATION_CHAIN_CHANGED,
        TYPE_ESCALATION_STEP_CREATED,
        TYPE_ESCALATION_STEP_DELETED,
        TYPE_ESCALATION_STEP_CHANGED,
        TYPE_MAINTENANCE_STARTED_FOR_ORGANIZATION,
        TYPE_MAINTENANCE_STARTED_FOR_INTEGRATION,
        TYPE_MAINTENANCE_STOPPED_FOR_ORGANIZATION,
        TYPE_MAINTENANCE_STOPPED_FOR_INTEGRATION,
        TYPE_MAINTENANCE_DEBUG_STARTED_FOR_ORGANIZATION,
        TYPE_MAINTENANCE_DEBUG_STARTED_FOR_INTEGRATION,
        TYPE_MAINTENANCE_DEBUG_STOPPED_FOR_ORGANIZATION,
        TYPE_MAINTENANCE_DEBUG_STOPPED_FOR_INTEGRATION,
        TYPE_CUSTOM_ACTION_CREATED,
        TYPE_CUSTOM_ACTION_DELETED,
        TYPE_CUSTOM_ACTION_CHANGED,
        TYPE_SCHEDULE_CREATED,
        TYPE_SCHEDULE_DELETED,
        TYPE_SCHEDULE_CHANGED,
        TYPE_ON_CALL_SHIFT_CREATED,
        TYPE_ON_CALL_SHIFT_DELETED,
        TYPE_ON_CALL_SHIFT_CHANGED,
        TYPE_NEW_USER_ADDED,
        TYPE_ORGANIZATION_SETTINGS_CHANGED,
        TYPE_USER_SETTINGS_CHANGED,
        TYPE_TELEGRAM_TO_USER_CONNECTED,
        TYPE_TELEGRAM_FROM_USER_DISCONNECTED,
        TYPE_API_TOKEN_CREATED,
        TYPE_API_TOKEN_REVOKED,
        TYPE_ESCALATION_CHAIN_COPIED,
        TYPE_SCHEDULE_EXPORT_TOKEN_CREATED,
        TYPE_MESSAGING_BACKEND_CHANNEL_CHANGED,
        TYPE_MESSAGING_BACKEND_CHANNEL_DELETED,
        TYPE_MESSAGING_BACKEND_USER_DISCONNECTED,
    ) = range(49)