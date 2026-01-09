from langchain.agents import create_agent
from .client import llm
from ..tools.book_tools import book_tools

# Crear el agente (más simple y moderno)
agent = create_agent(
    model=llm,
    tools=book_tools,
    system_prompt="""Eres un asistente especializado en gestión de libros.
    Puedes ayudar a crear, buscar, actualizar, eliminar y listar libros.
    Cuando el usuario te pida realizar operaciones sobre libros, usa las herramientas disponibles.
    Siempre sé claro y conciso en tus respuestas.
    Si necesitas información adicional para completar una tarea, pregunta al usuario."""
)

class IAService:
    """Servicio de IA para procesar consultas relacionadas con libros"""
    
    def __init__(self):
        self.agent = agent
    
    def process_query(self, query: str) -> str:
        """Procesa una consulta del usuario usando el agente con tools
        
        Args:
            query: Consulta o pregunta del usuario
            
        Returns:
            Respuesta del agente después de ejecutar las tools necesarias
        """
        result = self.agent.invoke({
            "messages": [{"role": "user", "content": query}]
        })
        
        # Extraer la última respuesta del agente
        return result["messages"][-1].content

# Instancia global del servicio
ia_service = IAService()
