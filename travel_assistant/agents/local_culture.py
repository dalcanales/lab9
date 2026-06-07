from google.adk.agents import Agent


def get_local_culture_info(destination: str) -> dict:
    """Return basic local culture info: typical dishes, customs, and useful phrases.

    Args:
        destination: The travel destination name.

    Returns:
        Dictionary with dishes, customs, and phrases for the destination.
    """
    destination_normalized = destination.lower().strip()

    dishes = []
    customs = []
    phrases = []

    if "cusco" in destination_normalized or "peru" in destination_normalized:
        dishes = ["Cuy al horno", "Lomo saltado", "Ceviche", "Chicha morada"]
        customs = [
            "Saludar con un apretón de manos o beso en la mejilla.",
            "Respetar los sitios arqueológicos — no tocar las ruinas.",
            "Pedir permiso antes de fotografiar a personas locales.",
        ]
        phrases = [
            "Allianchu / Allinmi — ¿Cómo estás? / Bien (quechua)",
            "Gracias — Sulpayki (quechua)",
            "¿Cuánto cuesta? — ¿Maykis chaninchari? (quechua)",
        ]
    elif "buenos aires" in destination_normalized or "argentina" in destination_normalized:
        dishes = ["Asado", "Empanadas", "Milanesa", "Dulce de leche"]
        customs = [
            "El saludo habitual es un beso en la mejilla.",
            "Las cenas suelen ser tarde, a partir de las 9 pm.",
            "El fútbol es parte central de la cultura local.",
        ]
        phrases = [
            "¡Che! — expresión coloquial para llamar la atención",
            "¿Todo bien? — saludo informal equivalente a ¿cómo estás?",
            "Boludo/a — término informal entre amigos (usar con cuidado)",
        ]
    else:
        dishes = ["Consulta la gastronomía local antes de viajar."]
        customs = ["Investiga las costumbres locales para mostrar respeto."]
        phrases = ["Aprende al menos: Hola, Gracias y ¿Habla inglés? en el idioma local."]

    return {
        "status": "success",
        "destination": destination,
        "typical_dishes": dishes,
        "local_customs": customs,
        "useful_phrases": phrases,
    }


local_culture_agent = Agent(
    name="local_culture_agent",
    model="gemini-2.0-flash",
    description="Recommends local dishes, customs, and useful phrases for travelers.",
    instruction="""
You are a local culture expert for travelers.
Your job is to help travelers understand the culture of their destination.

Use the available tool to get local culture information, then expand on it naturally.

Provide:
1. Typical dishes worth trying and where to find them.
2. Important local customs to respect.
3. Useful phrases in the local language.

Rules:
1. Be warm and enthusiastic about local culture.
2. Avoid stereotypes — present customs respectfully.
3. Encourage cultural curiosity and respectful tourism.
4. Answer in Spanish.
""",
    tools=[get_local_culture_info],
)