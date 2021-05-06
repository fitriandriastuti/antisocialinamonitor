import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import altair as alt

@st.cache #agar datanya bisa load secara real time
def load_data():
    df = pd.read_excel("antisocialina_labelling.xlsx", sheet_name='tweet_train')

    return df

def show_explore_page(df):
    st.title("Explore Tweet Labelling for Data Training")

    st.write(
        """
    ### Montioring Report of Tweet Labelling in Antisocialina
    """
    )

    data = df["classname"].value_counts()

    st.write(
        """
    #### Time Series Tweet Labelling of Antisocialina
    """
    )

    df_classname = df.groupby([df['created_at'].dt.date, df['classname']])['classname'].count().reset_index(
        name="jumlah")
    series = pd.DataFrame({
        'created_at': df_classname.created_at,
        'classname': df_classname.classname,
        'count': df_classname.jumlah
    })

    # Basic Altair line chart where it picks automatically the colors for the lines
    basic_chart = alt.Chart(series).mark_line().encode(
        x='created_at',
        y='count',
        color='classname',
        # legend=alt.Legend(title='Animals by year')
    )

    # Custom Altair line chart where you set color and specify dimensions
    custom_chart = alt.Chart(series).mark_line().encode(
        x='created_at',
        y='count',
        color=alt.Color('classname',
                        scale=alt.Scale(
                            domain=['Non-Antisosial / Umum',
                                    'Kegagalan untuk menyesuaikan diri dengan norma-norma sosial tentang perilaku yang sah',
                                    'Iritabilitas dan Agresivitas', 'Pengabaian yang gegabah untuk Keamanan',
                                    'Kurangnya Penyesalan'],
                            range=['blue', 'red', 'green', 'orange', 'purple'])
                        )
    ).properties(
        width=900,
        height=500
    )

    # st.altair_chart(basic_chart)
    st.altair_chart(custom_chart)

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.write("""#### Percentage of Tweet Labelling in Antisocialina""")

    st.pyplot(fig1)


    st.write(
        """
    #### Tweet Labelling of Antisocialina
    """
    )

    data = df.classname.value_counts().sort_values(ascending=False)
    st.bar_chart(data)



    # # df_timeseries = df.groupby(df.created_at.dt.date)
    # # df_classname = df.groupby([df['created_at'].dt.date, df['classname']], as_index=False)['classname'].count()
    # df_classname = df.groupby([df['created_at'].dt.date,df['classname']])['classname'].count().reset_index(name="count")
    # df_created_at = df.groupby([df['created_at'].dt.date], as_index=False).count()
    # df_timeseries2 = pd.DataFrame({
    #     'created_at': df_classname.created_at,
    #     'classname': df_classname.classname,
    #     # 'count': df_classname.count,
    # })
    #
    # # df_timeseries3 = df_timeseries2.rename(columns={'created_at': 'index'}).set_index('index')
    # # st.line_chart(df_timeseries3)


