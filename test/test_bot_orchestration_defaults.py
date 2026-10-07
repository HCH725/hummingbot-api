from models.bot_orchestration import V2ControllerDeployment, V2ScriptDeployment


APPROVED_HUMMINGBOT_IMAGE = "local/hummingbot:cb588082"


def test_script_deployment_defaults_to_approved_local_hummingbot_image():
    deployment = V2ScriptDeployment(
        instance_name="test_bot",
        credentials_profile="master_account",
    )
    assert deployment.image == APPROVED_HUMMINGBOT_IMAGE


def test_controller_deployment_defaults_to_approved_local_hummingbot_image():
    deployment = V2ControllerDeployment(
        instance_name="test_bot",
        credentials_profile="master_account",
        controllers_config=["controller_a"],
    )
    assert deployment.image == APPROVED_HUMMINGBOT_IMAGE
