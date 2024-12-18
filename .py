import streamlit as st
import pandas as pd
import resquest

if response.status_code == 200:
    countries = response.json()
    
    # Recorrer la lista de países y extraer los datos
    for country in countries:
        common_name = country['name'].get('common', 'N/A')
        region = country.get('region', 'N/A')
        population = country.get('population', 'N/A')
        area = country.get('area', 'N/A')
        borders = country.get('borders', [])
        languages = country.get('languages', {})
        timezones = country.get('timezones', [])
        
        # Extraer el número de fronteras, idiomas y zonas horarias
        num_borders = len(borders)
        num_languages = len(languages)
        num_timezones = len(timezones)
        
        # Imprimir los resultados
        print(f"País: {common_name}")
        print(f"Región: {region}")
        print(f"Población: {population}")
        print(f"Área: {area} km²")
        print(f"Número de fronteras: {num_borders}")
        print(f"Número de idiomas oficiales: {num_languages}")
        print(f"Número de zonas horarias: {num_timezones}")
        print("-" * 40)
else:
    print("Error al acceder a la API.")
