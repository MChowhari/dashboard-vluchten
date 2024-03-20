import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from streamlit_folium import folium_static



#data

airport= pd.read_csv('airports-extended-clean.csv', sep = ';')
flight1= pd.read_excel('1Flight 1.xlsx')
flight2= pd.read_excel('1Flight 2.xlsx')
flight3= pd.read_excel('1Flight 3.xlsx')
flight4= pd.read_excel('1Flight 4.xlsx')
flight5= pd.read_excel('1Flight 5.xlsx')
flight6= pd.read_excel('1Flight 6.xlsx')
flight7= pd.read_excel('1Flight 7.xlsx')
flight31= pd.read_excel('30Flight 1.xlsx')
flight32= pd.read_excel('30Flight 2.xlsx')
flight33= pd.read_excel('30Flight 3.xlsx')
flight34= pd.read_excel('30Flight 4.xlsx')
flight35= pd.read_excel('30Flight 5.xlsx')
flight36= pd.read_excel('30Flight 6.xlsx')
flight37= pd.read_excel('30Flight 7.xlsx')
schedule= pd.read_csv('schedule_airport.csv')

# Controleren als NaN of - in de dataframe zit en anders veranderen naar de de nul

schedule[["DL1", "IX1", "DL2", "IX2"]] = schedule[["DL1", "IX1", "DL2", "IX2"]].replace("-", "0")
flight1['TRUE AIRSPEED (derived)'].fillna(0, inplace=True)
flight2[['TRUE AIRSPEED (derived)', '[3d Latitude]', '[3d Longitude]', '[3d Altitude M]', '[3d Altitude Ft]', '[3d Heading]']] = flight3[['TRUE AIRSPEED (derived)', '[3d Latitude]', '[3d Longitude]', '[3d Altitude M]', '[3d Altitude Ft]', '[3d Heading]']].fillna(0)
flight3[['TRUE AIRSPEED (derived)', '[3d Latitude]', '[3d Longitude]', '[3d Altitude M]', '[3d Altitude Ft]', '[3d Heading]']] = flight3[['TRUE AIRSPEED (derived)', '[3d Latitude]', '[3d Longitude]', '[3d Altitude M]', '[3d Altitude Ft]', '[3d Heading]']].fillna(0)
flight4['TRUE AIRSPEED (derived)'].fillna(0, inplace=True)
flight5['TRUE AIRSPEED (derived)'].fillna(0, inplace=True)
flight6['TRUE AIRSPEED (derived)'].fillna(0, inplace=True)
flight7[['TRUE AIRSPEED (derived)', '[3d Latitude]', '[3d Longitude]', '[3d Altitude M]', '[3d Altitude Ft]', '[3d Heading]']] = flight3[['TRUE AIRSPEED (derived)', '[3d Latitude]', '[3d Longitude]', '[3d Altitude M]', '[3d Altitude Ft]', '[3d Heading]']].fillna(0)
flight32[['TRUE AIRSPEED (derived)', '[3d Latitude]', '[3d Longitude]', '[3d Altitude M]', '[3d Altitude Ft]', '[3d Heading]']] = flight3[['TRUE AIRSPEED (derived)', '[3d Latitude]', '[3d Longitude]', '[3d Altitude M]', '[3d Altitude Ft]', '[3d Heading]']].fillna(0)
flight33[['TRUE AIRSPEED (derived)', '[3d Latitude]', '[3d Longitude]', '[3d Altitude M]', '[3d Altitude Ft]', '[3d Heading]']] = flight3[['TRUE AIRSPEED (derived)', '[3d Latitude]', '[3d Longitude]', '[3d Altitude M]', '[3d Altitude Ft]', '[3d Heading]']].fillna(0)
flight34[['TRUE AIRSPEED (derived)', '[3d Latitude]', '[3d Longitude]', '[3d Altitude M]', '[3d Altitude Ft]', '[3d Heading]']] = flight3[['TRUE AIRSPEED (derived)', '[3d Latitude]', '[3d Longitude]', '[3d Altitude M]', '[3d Altitude Ft]', '[3d Heading]']].fillna(0)
flight36[['TRUE AIRSPEED (derived)', '[3d Latitude]', '[3d Longitude]', '[3d Altitude M]', '[3d Altitude Ft]', '[3d Heading]']] = flight3[['TRUE AIRSPEED (derived)', '[3d Latitude]', '[3d Longitude]', '[3d Altitude M]', '[3d Altitude Ft]', '[3d Heading]']].fillna(0)


# Controleren op duplicaten in de dataframe 
scheduleclean= schedule.drop_duplicates()
airportclean= airport.drop_duplicates()
flight1clean= flight1.drop_duplicates()
flight2clean= flight2.drop_duplicates()
flight3clean= flight3.drop_duplicates()
flight4clean= flight4.drop_duplicates()
flight5clean= flight5.drop_duplicates()
flight6clean= flight6.drop_duplicates()
flight7clean= flight7.drop_duplicates()
flight31clean= flight31.drop_duplicates()
flight32clean= flight32.drop_duplicates()
flight33clean= flight33.drop_duplicates()
flight34clean= flight34.drop_duplicates()
flight35clean= flight35.drop_duplicates()
flight36clean= flight36.drop_duplicates()
flight37clean= flight37.drop_duplicates()




# In[ ]:



# tabs die worden verwezen naar de onderstaande arguments

tab1, tab2, tab3, tab4, = st.tabs([":blue[Welkom]", ":blue[Vertraagde vluchten]", ":blue[Voorspellingen]", ":red[Conclusie]"])

# Voeg inhoud toe aan elke tab
with tab1:
    # Dit is het hoofd van de site
    st.title(':blue[Vertraagde vluchten :airplane:]')

    
    st.subheader('*Welkom bij onze luchtvaartanalysehub!*')

    st.write('Ontdek welke luchtvaartroutes wereldwijd het meest worden getroffen door vertragingen.      Van drukke binnenlandse vluchten tot internationale avonturen, we laten je de routes zien die je misschien wilt vermijden als je op tijd op je bestemming wilt aankomen.')

# URL van de afbeelding
    image_url = "https://xenforo.com/community/media/plane-jpg.2194/full"

# Afbeelding weergeven in Streamlit
    st.image(image_url, caption='Airplane', width=650)


    
with tab2:
    st.header("Mogelijke vertraagde vluchten") 
    st.subheader('*Verken de wereld met onze interactieve kaart:*') 
    st.write("Duik dieper in de luchtvaartwereld met onze interactieve kaart. Volg de routes met de     hoogste vertragingen en zoom in op specifieke regio's om te zien waar de problemen het grootst zijn.")
 
    # Subheader voor de Barplot in de zijbalk
    st.sidebar.subheader('🛬🛫 Vertraagde Vluchten')
    st.header('*Barplot*') 
    


    # Load and clean the data
   
    scheduleclean['STA_STD_ltc'] = pd.to_datetime(scheduleclean['STA_STD_ltc'])
    scheduleclean['ATA_ATD_ltc'] = pd.to_datetime(scheduleclean['ATA_ATD_ltc'])
    scheduleclean['Arrival_Status'] = scheduleclean['ATA_ATD_ltc'] - scheduleclean['STA_STD_ltc'] > pd.Timedelta(0)
    scheduleclean['Departure_Status'] = scheduleclean['STA_STD_ltc'] - scheduleclean['ATA_ATD_ltc'] > pd.Timedelta(0)

    # Calculate counts for the plot
    total_arrival_flights = len(scheduleclean[scheduleclean['LSV'].str.contains('L')])
    total_departure_flights = len(scheduleclean[scheduleclean['LSV'].str.contains('S')])
    arrival_delay_count = scheduleclean[scheduleclean['Arrival_Status'] & scheduleclean['LSV'].str.contains('L')].shape[0]
    arrival_ontime_count = total_arrival_flights - arrival_delay_count
    departure_delay_count = scheduleclean[scheduleclean['Departure_Status'] & scheduleclean['LSV'].str.contains('S')].shape[0]
    departure_ontime_count = total_departure_flights - departure_delay_count

    # Calculate percentages
    arrival_delay_percent = round(arrival_delay_count / total_arrival_flights * 100, 1)
    arrival_ontime_percent = round(arrival_ontime_count / total_arrival_flights * 100, 1)
    departure_delay_percent = round(departure_delay_count / total_departure_flights * 100, 1)
    departure_ontime_percent = round(departure_ontime_count / total_departure_flights * 100, 1)

    # Create a DataFrame for the plot
    data_arrival = {
        'Vlucht Status': ['Vertraagd bij Aankomst', 'Aankomst op Tijd'],
        'Aantal Vluchten': [arrival_delay_count, arrival_ontime_count],
        'Percentage': [arrival_delay_percent, arrival_ontime_percent]
    }
    df_arrival = pd.DataFrame(data_arrival)

    data_departure = {
        'Vlucht Status': ['Vertraagd bij Vertrek', 'Tijdig Vertrek'],
        'Aantal Vluchten': [departure_delay_count, departure_ontime_count],
        'Percentage': [departure_delay_percent, departure_ontime_percent]
    }
    df_departure = pd.DataFrame(data_departure)

    # Define colors
    delay_color = '#069AF3'
    ontime_color = '#13EAC9'

    # Sidebar
    st.sidebar.subheader('Barplot')
    selected_option = st.sidebar.selectbox('Kies een optie', ['Aankomst', 'Vertrek'])

    # Map opties naar kleuren
    color_map_arrival = {'Vertraagd bij Aankomst': delay_color, 'Aankomst op Tijd': ontime_color}
    color_map_departure = {'Vertraagd bij Vertrek': delay_color, 'Tijdig Vertrek': ontime_color}

    # Create the plot using Plotly Express
    if selected_option == 'Aankomst':
        fig = px.bar(df_arrival, x='Vlucht Status', y='Aantal Vluchten', text='Percentage',
                     color='Vlucht Status',
                     color_discrete_map=color_map_arrival,
                     labels={'Aantal Vluchten': 'Aantal Vluchten', 'Percentage': 'Percentage'},
                     title='Aantal Vluchten Verdeeld over Aankomst Status')
    else:
        fig = px.bar(df_departure, x='Vlucht Status', y='Aantal Vluchten', text='Percentage',
                     color='Vlucht Status',
                     color_discrete_map=color_map_departure,
                     labels={'Aantal Vluchten': 'Aantal Vluchten', 'Percentage': 'Percentage'},
                     title='Aantal Vluchten Verdeeld over Vertrek Status')

    # Show the plot
    st.plotly_chart(fig)
    st.write('*:blue[Conclusion out of the graph:]*')
    st.write('Vertraging is vaker veroorzaakt op outstations, arrival delays/on time is 51.4%/48.6%. Grondafhandeling in ZRH is goed! Het aantal departure delays is namelijk erg verminderd tot een verhouding van ongeveer 20.8%/79.2%')
    
    st.header('*Location*') 
    
    # Convert 'STA_STD_ltc' and 'ATA_ATD_ltc' to datetime format
    scheduleclean['STA_STD_ltc'] = pd.to_datetime(scheduleclean['STA_STD_ltc'])
    scheduleclean['ATA_ATD_ltc'] = pd.to_datetime(scheduleclean['ATA_ATD_ltc'])

    # Calculate the delay in seconds
    scheduleclean['Delay_seconds'] = (scheduleclean['ATA_ATD_ltc'] - scheduleclean['STA_STD_ltc']).dt.total_seconds()

    # Convert delay to timedeltas with custom formatting
    scheduleclean['Delay'] = pd.to_timedelta(scheduleclean['Delay_seconds'], unit='s')

    # Add '+' or '-' sign manually based on delay
    scheduleclean['Delay'] = scheduleclean['Delay'].apply(lambda x: ('+' if x >= pd.Timedelta(0) else '-') + str(abs(x)))

    # Drop the temporary column
    scheduleclean.drop(columns=['Delay_seconds'], inplace=True)

    # Convert 'Delay' column to numeric format (hours)
    scheduleclean['Delay_hours'] = pd.to_timedelta(scheduleclean['Delay']).dt.total_seconds() / 3600

    # Grouping by Location and calculating the average Delay
    avg_delay_per_location = scheduleclean.groupby('Org/Des')['Delay_hours'].mean().reset_index()

    # Renaming the columns for clarity
    avg_delay_per_location.columns = ['Org/Des', 'Average_Delay_hours']

    # Displaying the resulting DataFrame
    st.table(avg_delay_per_location)
    
    st.header('*Scatterplot*') 

    # Filter the dataset for values with 'S' in the 'LSV' column
    departure_data = scheduleclean[scheduleclean['LSV'] == 'S']

    # Filter the dataset for values with a '+' sign in the 'Delay' column
    positive_delay_data = departure_data[departure_data['Delay'].str.startswith('+')]

    # Extract departure time in minutes past midnight
    departure_time_minutes = positive_delay_data['ATA_ATD_ltc'].dt.hour * 60 + positive_delay_data['STA_STD_ltc'].dt.minute

    # Extract delay minutes from the 'Delay' column
    delay_minutes = positive_delay_data['Delay'].str.extract(r'\+(\d+) days (\d+):(\d+):').astype(float)
    delay_minutes = delay_minutes[1] * 60 + delay_minutes[2]  # Convert hours to minutes and add minutes

    # Calculate mean delay
    mean_delay = delay_minutes.mean()

    # Create dataframe for Plotly scatterplot
    scatter_data = pd.DataFrame({'Departure_Time': departure_time_minutes, 'Delay': delay_minutes})

    # Create interactive scatterplot
    fig = px.scatter(scatter_data, x='Departure_Time', y='Delay', color='Delay', labels={'Departure_Time': 'Vertrektijd (uren)', 'Delay': 'Vertraging (minuten)'},
                     title='Relatie tussen vertraging en vertrektijd',
                     hover_data={'Departure_Time': False, 'Delay': True}, trendline='ols')  

    # Change color of trend line to red
    fig.update_traces(line=dict(color='red'))

    # Add mean line
    fig.add_hline(y=mean_delay, line_dash="dash", line_color="orange", annotation_text=f"Mean Delay: {mean_delay:.2f} minuten", annotation_position="bottom right", annotation_y=0.6)

    # Customize x-axis tick values and labels
    tick_values = list(range(int(departure_time_minutes.min()), int(departure_time_minutes.max()) + 1, 120))  # Every 2 hours
    tick_labels = [f"{h//60:02d}:{h%60:02d}" for h in tick_values]  # Format tick labels as HH:MM
    fig.update_xaxes(tickvals=tick_values, ticktext=tick_labels)

    # Update layout to make the graph bigger
    fig.update_layout(height=600, width=600, showlegend=False)

    # Display the plot in Streamlit
    st.plotly_chart(fig)

    
    
    
    
    

with tab3:
    st.header("Voorspellingen")
    st.subheader("*Voorspel vertragingen op je volgende vlucht:*")
    st.write("Ben je van plan om binnenkort te vliegen? Gebruik onze voorspellingsmodule om te zien hoeveel vertraging je kunt verwachten op jouw specifieke route. Met behulp van geavanceerde modellen kunnen we je een nauwkeurige inschatting geven, zodat je goed voorbereid op reis kunt gaan!")
# Voorbeeld DataFrame
    

 
    
   

   
 

    
    
    

 
    




with tab4:
 
    # Display header
   
    st.header('*Location*')

    # Convert 'STA_STD_ltc' and 'ATA_ATD_ltc' to datetime format
    scheduleclean['STA_STD_ltc'] = pd.to_datetime(scheduleclean['STA_STD_ltc'])
    scheduleclean['ATA_ATD_ltc'] = pd.to_datetime(scheduleclean['ATA_ATD_ltc'])

    # Calculate the delay in seconds
    scheduleclean['Delay_seconds'] = (scheduleclean['ATA_ATD_ltc'] - scheduleclean['STA_STD_ltc']).dt.total_seconds()

    # Convert delay to timedeltas with custom formatting
    scheduleclean['Delay'] = pd.to_timedelta(scheduleclean['Delay_seconds'], unit='s')

    # Add '+' or '-' sign manually based on delay
    scheduleclean['Delay'] = scheduleclean['Delay'].apply(lambda x: ('+' if x >= pd.Timedelta(0) else '-') + str(abs(x)))

    # Drop the temporary column
    scheduleclean.drop(columns=['Delay_seconds'], inplace=True)

    # Convert 'Delay' column to numeric format (hours)
    scheduleclean['Delay_hours'] = pd.to_timedelta(scheduleclean['Delay']).dt.total_seconds() / 3600

    # Grouping by Location and calculating the average Delay
    avg_delay_per_location = scheduleclean.groupby('Org/Des')['Delay_hours'].mean().reset_index()

    # Renaming the columns for clarity
    avg_delay_per_location.columns = ['Org/Des', 'Average_Delay_hours']

    # Dropdown menu to select which location to display
    st.sidebar.subheader('Location')
    selected_location = st.sidebar.selectbox('Selecteer een locatie', avg_delay_per_location['Org/Des'].unique())

    # Filter data for the selected location
    selected_data = avg_delay_per_location[avg_delay_per_location['Org/Des'] == selected_location]

    # Display selected data
    if not selected_data.empty:
        st.write(f"Gemiddelde vertraging voor locatie '{selected_location}': {selected_data.iloc[0]['Average_Delay_hours']:.2f} uur")
    else:
        st.write("Geen gegevens beschikbaar voor deze locatie.")
        
