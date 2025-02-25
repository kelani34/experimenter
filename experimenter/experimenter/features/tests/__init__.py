import os
import pathlib

from django.test import override_settings

mock_valid_features = override_settings(
    FEATURE_MANIFESTS_PATH=os.path.join(
        pathlib.Path(__file__).parent.absolute(), "fixtures", "valid_features"
    )
)

mock_invalid_features = override_settings(
    FEATURE_MANIFESTS_PATH=os.path.join(
        pathlib.Path(__file__).parent.absolute(), "fixtures", "invalid_features"
    )
)

mock_remote_schema_features = override_settings(
    FEATURE_MANIFESTS_PATH=os.path.join(
        pathlib.Path(__file__).parent.absolute(), "fixtures", "remote_schema_features"
    )
)

mock_invalid_remote_schema_features = override_settings(
    FEATURE_MANIFESTS_PATH=os.path.join(
        pathlib.Path(__file__).parent.absolute(),
        "fixtures",
        "invalid_remote_schema_features",
    )
)
