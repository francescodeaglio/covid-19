import datetime
from functools import partial

from covid_19.dashboard_field.dashboard_screen import DashboardScreen
from covid_19.dashboard_field.utils import get_norm_data, transform_regions_pc_to_human_all, determina_scelte, st_functional_columns
from covid_19.dashboard_field.vaccini.chart_barvaccini import ChartBarVaccini
from covid_19.dashboard_field.vaccini.chart_barvacciniitalia import ChartBarVacciniItalia
from covid_19.dashboard_field.vaccini.chart_barvax import ChartBarVax
from covid_19.dashboard_field.vaccini.chart_percentagemap import ChartPercentageMap
from covid_19.dashboard_field.vaccini.chart_pydeckmap import ChartPydeckMap
import streamlit as st

from covid_19.dashboard_field.vaccini.chart_tempform import ChartTempForm


class ScreenVaccini(DashboardScreen):

    def __init__(self, title, name, chart_list=None, subtitle=None, widget_list = None):
        super().__init__(title,name,chart_list,subtitle, widget_list)
        self.chart_dict = {}
        self.data = get_norm_data()

    def show_charts(self):



        """
        name = "Andamento vaccinazioni per categorie a livello nazionale"
        subtitle = "In questo grafico è possibile selezionare un mese. Verrà mostrato, giorno per giorno, il numero di" \
                   " vaccini effettuati per ogni categoria. Passando con il mouse sopra il grafico è possibile leggere i valori esatti."
        dati = "https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-summary-latest.csv"

        ChartBarVacciniItalia(name, name, subtitle, dati).show()


        exp = st.beta_expander("Espandi per visualizzare le informazioni a livello regionale")
        name = "Andamento vaccinazioni per categorie a livello regionale"
        subtitle= "In questo grafico è possibile selezionare una specifica regione e un mese. Verrà mostrato, giorno per giorno, il numero di" \
                  " vaccini effettuati per ogni categoria. Passando con il mouse sopra il grafico è possibile leggere i valori esatti."
        dati = "https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-summary-latest.csv"

        ChartBarVaccini(name, name, subtitle, dati, posizione=exp).show()

        name = "Somministrazione per case farmaceutiche"
        subtitle = "In questo grafico viene mostrato, categoria per categoria, il numero di dosi somministrate per ogni tipo di vaccino a disposizione."
        dati = "https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-latest.csv"

        ChartBarVax(name, name, subtitle, dati).show()
        """

        name = "Andamento temporale somministrazione per case farmaceutiche"
        subtitle = "In questo grafico viene mostrato l'andamento temporale del numero di dosi somministrate per ogni tipo di vaccino a disposizione."
        dati = "https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-latest.csv"

        ChartTempForm(name, name, subtitle, dati).show()

        name = "Percentuale somministrazione vaccini a livello regionale"
        subtitle = "In questa mappe è possibile visualizzare l'andamento dei vaccini sul totale della popolazione interessata. E' possibile selezionare" \
                   " la categoria dalla selectbox qui sotto. Attenzione: i dati di questo grafico non sono aggiornati quotidianamente ma a cadenza settimanale."
        dati = "https://raw.githubusercontent.com/camicius/covid19-opendata-vaccini-sqlite/main/reportsettimanali.csv"

        ChartPercentageMap(name, name, subtitle, dati).show()

        # primo grafico: Mappa 3d dei vaccini
        name = "Mappa andamento nazionale"
        subtitle = "La mappa mostra l'andamento delle regioni italiane nella somministrazione dei vaccini. L'altezza della regione" \
                   " è determinata dal numero di dosi somministrate mentre il colore dipende dalla percentuale di somministrazione rispetto alle dosi ricevute (giallo: bassa percentuale, rosso: alto)." \
                   " Passando con il cursore sopra le regioni è possibile vedere i valori dei due andamenti citati."
        dati = "https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/vaccini-summary-latest.csv"

        ChartPydeckMap(name, name, subtitle, dati).show()

        """
        # controllo se ho i dati aggiornati. Se sono aggiornati bene, altrimenti scarica i nuovi
        self.data = get_norm_data()
        #massimi e confronti
        name = "Andamento temporale e massimi"
        subtitle = "In questo grafico interattivo puoi selezionare il periodo (direttamente sul grafico), le regioni e il parametro (dai widget)."
        arg = [["multiselect", "Seleziona la regione", transform_regions_pc_to_human_all()],
               ["selectbox", "Quale parametro vuoi confrontare?", determina_scelte(self.data.norm_regions_df_ita)]]
        wl = [ partial(st_functional_columns, arg)]
        ChartInterattivo(name, name, subtitle, self.data, widget_list=wl).show()

        #mappa
        name = "Mappa parametrizzata"
        subtitle = "In questo grafico puoi selezionare il giorno e il parametro e vedere l'andamento regione per regione sulla mappa."
        min = datetime.datetime.fromisoformat(str(self.data.norm_regions_df_ita.data.min()))
        max = datetime.datetime.fromisoformat(str(self.data.norm_regions_df_ita.data.max()))
        arg = [["date_input","seleziona il giorno", max, min, max],
               ["selectbox", "Quale parametro vuoi valutare?", determina_scelte(self.data.norm_regions_df_ita)]]
        wl = [ partial(st_functional_columns, arg)]
        ChartMapPlotly(name, name, subtitle, self.data, widget_list=wl).show()

        #piechart
        name = "Grafico a torta"
        subtitle = "In questo grafico è possibile visualizzare come si è suddiviso il numero di un certo parametro tra diverse regioni." \
                   " E' possibile selezionare una lista di regioni, il giorno, il parametro e la libreria grafica."

        scelte_ammissibili = list(filter(lambda t: "nuovi" not in t, determina_scelte(self.data.norm_regions_df_ita)))

        arg = [
            ["selectbox", "Scegli la libreria", ["Bokeh", "Pyplot"]],
             ["selectbox", "Scegli il parametro da valutare", scelte_ammissibili],
             ["date_input", "Scegli il giorno", max, min, max],
             ["multiselect", "Seleziona le regioni", transform_regions_pc_to_human_all()]
        ]
        wl = [partial(st_functional_columns, arg, (0.15,0.30,0.20,0.35))]
        ChartPie(name, name, subtitle, self.data, widget_list=wl).show()"""