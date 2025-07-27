import streamlit as st
from datetime import datetime
import pytz

# Definir zona horaria CET
CET = pytz.timezone('CET')

# Obtener la fecha y hora actual en la zona horaria CET
now = datetime.now()

st.write(now)

# Fecha límite (28 de julio)
limit_date = datetime(now.year, 7, 28, tzinfo=CET)
limit_date2 = datetime(now.year, 7, 29, tzinfo=CET)

st.title("⚽ ¿Puede Chuchi renovar ya el carnet del Pucela? ⚽")

# Lógica para mostrar el mensaje adecuado
if now < limit_date:
    st.write("⌛ Todavía no es 28 de Julio.")
    st.write("Aunque puede haber sorpresas, si Mas, Soler o Romeo dan la sorpresa y ganan una etapa.")
    st.write("Pero tranquilo, tampoco ha renovado Sergio, hay tiempo de comer. Dani ha hecho los deberes.")
    st.write(now)
    st.write(limit_date)
elif now < limit_date2:
    st.write("💜 Ya puede, es 28 de Julio")
else:
    st.write("Seguro que ya renovó")
