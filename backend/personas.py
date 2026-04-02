"""
Roast Council - Persona Loader
Loads persona definitions from persona.json for dynamic configuration.
"""
import json
import os

def load_personas():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(base_dir, 'persona.json')
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    except Exception as e:
        print(f"[ERROR] Failed to load persona.json: {e}")
        # Fallback minimal config if file missing
        return {
            "hater": {
                "name": "The Hater",
                "emoji": "😤", 
                "system_prompt": "You are a hater. Roast them.",
                "fallback": "Hater offline."
            }
        }

PERSONAS = load_personas()


def get_persona_list():
    """
    Returns a list of persona metadata for the frontend.
    
    Returns:
        list: [{"id": "hater", "name": "The Hater", "emoji": "😤"}, ...]
    """
    return [
        {
            "id": persona_id,
            "name": data["name"],
            "emoji": data["emoji"]
        }
        for persona_id, data in PERSONAS.items()
    ]


def get_persona(persona_id):
    """
    Get a specific persona's data.
    
    Args:
        persona_id: ID of the persona (e.g., "hater")
    
    Returns:
        dict: Persona data or None if not found
    """
    return PERSONAS.get(persona_id)


# For backwards compatibility (if any code still tries to import PersonaManager)
class PersonaManager:
    """
    Deprecated: Kept for backwards compatibility only.
    Use PERSONAS dict directly instead.
    """
    def __init__(self):
        self.personas = PERSONAS
        print("[WARN] PersonaManager is deprecated. Use PERSONAS dict directly.")
    
    def get_all_persona_names(self):
        return list(PERSONAS.keys())
