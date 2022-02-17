import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import pandas as pd
import cufflinks as cf
import seaborn as sns
import plotly
import plotly.figure_factory as ff
import chart_studio.plotly as py
import plotly.graph_objects as go
import plotly.express as px


st.title("MSBA 325 Assignment")
st.image("https://www.aub.edu.lb/osb/UndergradProgram/Undergrad%20Rotator/Bldg1.jpg")
st.markdown("The first section includes the visualizations of the tutorials previously submitted")


trial = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/school_earnings.csv")

#to plot a bar chart of the different school gaps
data = [go.Bar(x=trial.School,
            y=trial.Gap)]
st.plotly_chart(data, use_container_width=True)

#To plot average earning of graduates
trace_women = go.Bar(x=trial.School,
                  y=trial.Women,
                  name='Women',
                  marker=dict(color='#ffcdd2'))

trace_men = go.Bar(x=trial.School,
                y=trial.Men,
                name='Men',
                marker=dict(color='#A2D5F2'))

trace_gap = go.Bar(x=trial.School,
                y=trial.Gap,
                name='Gap',
                marker=dict(color='#59606D'))

data = [trace_women, trace_men, trace_gap]

layout = go.Layout(title="Average Earnings for Graduates",
                xaxis=dict(title='School'),
                yaxis=dict(title='Salary (in thousands)'))

fig = go.Figure(data=data, layout=layout)
st.plotly_chart(fig, use_container_width=True)

#to plot the parametric plot
s = np.linspace(0, 2 * np.pi, 240)
t = np.linspace(0, np.pi, 240)
tGrid, sGrid = np.meshgrid(s, t)

r = 2 + np.sin(7 * sGrid + 5 * tGrid)  # r = 2 + sin(7s+5t)
x = r * np.cos(sGrid) * np.sin(tGrid)  # x = r*cos(s)*sin(t)
y = r * np.sin(sGrid) * np.sin(tGrid)  # y = r*sin(s)*sin(t)
z = r * np.cos(tGrid)                  # z = r*cos(t)

surface = go.Surface(x=x, y=y, z=z)
data = [surface]

layout = go.Layout(
    title='Parametric Plot',
    scene=dict(
        xaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        yaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        zaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        )
    )
)

figg = go.Figure(data=data, layout=layout)
st.plotly_chart(figg, use_container_width=True)

#to plot changing frequency graph
data = [dict(
        visible = False,
        line=dict(color='#00CED1', width=6),
        name = '𝜈 = '+str(step),
        x = np.arange(0,10,0.01),
        y = np.sin(step*np.arange(0,10,0.01))) for step in np.arange(0,5,0.1)]
data[10]['visible'] = True

steps = []
for i in range(len(data)):
    step = dict(
        method = 'restyle',
        args = ['visible', [False] * len(data)],
    )
    step['args'][1][i] = True # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active = 10,
    currentvalue = {"prefix": "Frequency: "},
    pad = {"t": 50},
    steps = steps
)]

layout = dict(sliders=sliders)
fig1 = dict(data=data, layout=layout)
st.plotly_chart(fig1, use_container_width=True)

#to plot continent gd per capital against life expectancy
df = px.data.gapminder()
fig2=px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="continent", hover_name="country",
           log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])
st.plotly_chart(fig2, use_container_width=True)

#to plot population in different continents
df = px.data.gapminder()

fig3 = px.bar(df, x="continent", y="pop", color="continent",
  animation_frame="year", animation_group="country", range_y=[0,4000000000])
st.plotly_chart(fig3, use_container_width=True)

st.markdown("The second section includes the visuzalations of airbnb dataset ")


#trying to read csv 
import io
    
# Downloading the csv file from your GitHub account

url = "https://github.com/sarard2/kiki/blob/main/US.csv" # Make sure the url is the raw version of the file on GitHub
download = requests.get(url).content

# Reading the downloaded content and turning it into a pandas dataframe

df = pd.read_csv(io.StringIO(download.decode('utf-8')))

#Visualizations related to me
urll="https://github.com/sarard2/kiki/blob/main/NY.csv"
downloadd=requests.get(urll).content
df1=pd.read_csv(io.StringIO(downloadd.decode('utf-8')))

#to plot average prices among room types
df1private=df1.groupby("room_type").mean("price")
modifieddf1=df1private.reset_index()
figure = px.bar(modifieddf1, x='room_type', y='price',color='minimum_nights',title="Average Prices Among Room Types")
st.plotly_chart(figure, use_container_width=True)

#to plot average ratings among property Types
dfprivate=df.groupby("property_type").mean("review_scores_rating")
modifieddf=dfprivate.reset_index()
figure1 = px.bar(modifieddf, x='property_type', y='review_scores_rating',color='number_of_reviews',title="Average Ratings Among Property Types")
st.plotly_chart(figure1, use_container_width=True)

#to plot average price among neighbourhood
df_neighbourhood=df1.groupby("neighbourhood").mean()
modified=df_neighbourhood.reset_index()
figure2 = px.bar(modified, x='neighbourhood', y='price',color='neighbourhood',title="Average Price Among Neighbourhood")
st.plotly_chart(figure2, use_container_width=True)

#lineplot
df_price=df1.groupby("price").mean("minimum_nights")
modifiedd=df_price.reset_index()
figure3=px.line(modifiedd,x="price",y=["number_of_reviews","minimum_nights"])
st.plotly_chart(figure3, use_container_width=True)

#3d plot
figure4 = px.scatter_3d(df, x="accommodates", y=df.number_of_reviews, z=df.review_scores_rating,
              color="cancellation_policy")
st.plotly_chart(figure4, use_container_width=True)

#map
map = px.density_mapbox(df, lat = "latitude", lon ="longitude", z = "review_scores_rating", radius = 10,
                       center = dict(lat = 9, lon =8), zoom = 1, hover_name = 'room_type',
                       mapbox_style = 'open-street-map', title = 'US Airbnb Map')
st.plotly_chart(map, use_container_width=True)

#scatter
scatter=px.scatter(df1, x="price", y="number_of_reviews", animation_frame="calculated_host_listings_count", animation_group="neighbourhood",
           color="room_type", hover_name="room_type",
           log_x=True, size_max=55, range_x=[10,1000], range_y=[25,90])
st.plotly_chart(scatter, use_container_width=True)
