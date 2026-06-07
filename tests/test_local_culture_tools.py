from travel_assistant.agents.local_culture import get_local_culture_info


def test_local_culture_cusco():
    result = get_local_culture_info("Cusco")
    assert result["status"] == "success"
    assert len(result["typical_dishes"]) > 0
    assert len(result["local_customs"]) > 0
    assert len(result["useful_phrases"]) > 0


def test_local_culture_default_destination():
    result = get_local_culture_info("Tokio")
    assert result["status"] == "success"
    assert result["destination"] == "Tokio"
    assert len(result["typical_dishes"]) >= 1


def test_local_culture_argentina():
    result = get_local_culture_info("Buenos Aires")
    assert result["status"] == "success"
    assert any("Asado" in dish for dish in result["typical_dishes"])