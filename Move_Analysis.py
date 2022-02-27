# Import Packs<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

#####################################################################################################################
# load the data(tmdb-movies.csv)<<<<<<<<<<<<<<<<
tmdb_data = pd.read_csv("mdb-movies.csv")
tmdb_data.head()
#####################################################################################################################
# pd.set_option('display.max_rows', tmdb_data.shape[0] + 1)
# pd.set_option('display.max_columns', tmdb_data.shape[0] + 1)
#####################################################################################################################
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Data Cleaning<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# data describe
tmdb_describe = tmdb_data.describe()
#####################################################################################################################
# data_info_1
# tmdb_info_1 = tmdb_data.info()
# print("="*80)
#####################################################################################################################
# Delete Columns
delete_columns = ["id", "imdb_id", "popularity", "homepage", "release_year", "tagline", "overview", "vote_count",
                  "vote_average", "budget_adj", "revenue_adj", "keywords"]
tmdb_data.drop(delete_columns, axis=1, inplace=True)
#####################################################################################################################
# Date_time
tmdb_data["release_date"] = pd.to_datetime(tmdb_data["release_date"])
#####################################################################################################################
# Remove_Duplicated
tmdb_duple = tmdb_data.duplicated()
tmdb_data.drop_duplicates(keep='first', inplace=True)
#####################################################################################################################
# REmove_Zero_Values
tmdb_data[["revenue", "budget"]] = tmdb_data[["revenue", "budget"]].replace(0, np.nan)
tmdb_data.dropna(subset=["revenue", "budget"], inplace=True)
tmdb_data['runtime'] = tmdb_data['runtime'].replace(0, np.NaN)
#####################################################################################################################
# data_info_2
# tmdb_info_2 = tmdb_data.info()
#####################################################################################################################
#####################################################################################################################
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Analysis<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Analysis<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
# Heat Map Correlation
data_plot = sb.heatmap(tmdb_data.corr(), annot=True)
plt.show()
#-----------------------------------------------------------
# Profit
tmdb_data["profit"] = tmdb_data["revenue"] - tmdb_data["budget"]
print("Movie with highest profit :", "\n", tmdb_data.loc[tmdb_data["profit"].idxmax()])
print("=" * 80)
print("Movie with Lowest profit :", "\n", tmdb_data.loc[tmdb_data["profit"].idxmin()])
print("=" * 80)
print("The average profit of the movies :", tmdb_data["profit"].mean())
print("=" * 80)
#####################################################################################################################
# Budget
print("=" * 80)
print("Movie with highest budget :", "\n", tmdb_data.loc[tmdb_data["budget"].idxmax()])
print("=" * 80)
print("Movie with highest budget :", "\n", tmdb_data.loc[tmdb_data["budget"].idxmax()])
print("=" * 80)
print("The average budget of the movies :", tmdb_data["budget"].mean())
print("=" * 80)
#--------------------------
# x-axis
plt.xlabel('Budget in Dollars')
# y-axis
plt.ylabel('Profit in Dollars')
# Title of the histogram
plt.title('Relationship between budget and profit')
plt.scatter(tmdb_data['budget'], tmdb_data['profit'], alpha=0.5)
plt.show()
#####################################################################################################################
# Revenue
print("Movie with highest revenue :", "\n", tmdb_data.loc[tmdb_data["revenue"].idxmax()])
print("=" * 80)
print("Movie with highest revenue :", "\n", tmdb_data.loc[tmdb_data["revenue"].idxmax()])
print("=" * 80)
print("The average revenue of the movies :", tmdb_data["revenue"].mean())
print("=" * 80)
#--------------------------
# x-axis
plt.xlabel('Revenue in Dollars')
# y-axis
plt.ylabel('Profit in Dollars')
# Title of the histogram
plt.title('Relationship between revenue and profit')
plt.scatter(tmdb_data['revenue'], tmdb_data['profit'], alpha=0.5)
plt.show()
#####################################################################################################################
# Run time
print("The height runtime  movie :", "\n", tmdb_data.loc[tmdb_data["runtime"].idxmax()])
print("=" * 80)
print("The low runtime  movie :", "\n", tmdb_data.loc[tmdb_data["runtime"].idxmin()])
print("=" * 80)
print("The average runtime of the movies :", tmdb_data["runtime"].mean())
print("=" * 80)
#--------------------------
# x-axis
plt.xlabel('Runtime in Minutes')
# y-axis
plt.ylabel('Profit in Dollars')
# Title of the histogram
plt.title('Relationship between runtime and profit')
plt.scatter(tmdb_data['runtime'], tmdb_data['profit'], alpha=0.5)
plt.show()
#####################################################################################################################
# Genres
genres_count = pd.Series(tmdb_data['genres'].str.cat(sep='|').split('|')).value_counts(ascending=False)
print("the Top Genres are : ", "\n", genres_count)
diagram = genres_count.plot.bar(fontsize=8)
# Set a title
diagram.set(title='Top Genres General')
# x-label and y-label
diagram.set_xlabel('Type of genres')
diagram.set_ylabel('Number of Movies')
# Show the plot
plt.show()
print("=" * 80)


#####################################################################################################################
# Cast
cast_count = pd.Series(tmdb_data['cast'].str.cat(sep='|').split('|')).value_counts(ascending=False)
print("the Top Cast are that we can work with it : ", "\n", cast_count)
diagram_cast = cast_count.head(20).plot.barh(fontsize=8)
# Set a title
diagram_cast.set(title='Top Cast Genral')
# x-label and y-label
diagram_cast.set_xlabel('Number of Movies')
diagram_cast.set_ylabel('List of cast')
# Show the plot
plt.show()
print("=" * 80)
#####################################################################################################################
# Production_companies
production_companies_count = pd.Series(tmdb_data['production_companies'].str.cat(sep='|').split('|')).value_counts(
    ascending=False)
print("the Top Production_companies are that we can work with it : ", "\n", production_companies_count)
diagram_production_companies = production_companies_count.head(20).plot.barh(fontsize=8)
# Set a title
diagram_production_companies.set(title='Top  production companies ')
# x-label and y-label
diagram_production_companies.set_xlabel('Number of Movies')
diagram_production_companies.set_ylabel('List of cast')
# Show the plot
plt.show()
print("=" * 80)
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Deep_Analysis<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Deep_Analysis<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
# If you want to make profit between next conditions:
conditions = [
    tmdb_data["profit"] <= tmdb_data["profit"].mean() - (tmdb_data["profit"].std() + tmdb_data["profit"].std()),
    tmdb_data["profit"] <= tmdb_data["profit"].mean() - tmdb_data["profit"].std(),
    tmdb_data["profit"] <= tmdb_data["profit"].mean(),
    tmdb_data["profit"] <= tmdb_data["profit"].mean() + tmdb_data["profit"].std(),
    tmdb_data["profit"] > tmdb_data["profit"].mean() + (tmdb_data["profit"].std() + tmdb_data["profit"].std())]
values = ["D", "C", "B", "A", "AA"]
tmdb_data["Class"] = np.select(conditions, values)
#####################################################################################################################
# if you want to make D class move
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Make D class move<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
tmdb_data_class_D = tmdb_data[tmdb_data["Class"] == "D"]
# -------------------------------------
print("The average budget of the movie will be :", tmdb_data_class_D["budget"].mean())
print("=" * 80)
print("The average revenue of the movie will be  :", tmdb_data_class_D["revenue"].mean())
print("=" * 80)
print("The average profit of the movie will be :", tmdb_data_class_D["profit"].mean())
print("=" * 80)
print("The average runtime of the movie will be :", tmdb_data_class_D["runtime"].mean())
print("=" * 80)
# -------------------------------------
genres_count_class_D = pd.Series(tmdb_data_class_D['genres'].str.cat(sep='|').split('|')).value_counts(ascending=False)
print("the Top 10 Genres are : ", "\n", genres_count_class_D.head(10))
print("=" * 80)
diagram_genres_D = genres_count_class_D.plot.bar(fontsize=8)
# Set a title
diagram_genres_D.set(title='Top Genres class_D')
# x-label and y-label
diagram_genres_D.set_xlabel('Type of genres')
diagram_genres_D.set_ylabel('Number of Movies')
# Show the plot
plt.show()
# -------------------------------------
cast_count_class_D = pd.Series(tmdb_data_class_D['cast'].str.cat(sep='|').split('|')).value_counts(ascending=False)
print("the Top 10 Cast are that we can work with it : ", "\n", cast_count_class_D.head(10))
diagram_cast_D = cast_count_class_D.head(20).plot.barh(fontsize=8)
# Set a title
diagram_cast_D.set(title='Top Cast class D')
# x-label and y-label
diagram_cast_D.set_xlabel('Number of Movies')
diagram_cast_D.set_ylabel('List of cast')
# Show the plot
plt.show()
print("=" * 80)
# -------------------------------------
production_companies_count_class_D = pd.Series(
    tmdb_data_class_D['production_companies'].str.cat(sep='|').split('|')).value_counts(ascending=False)
print("the Top 10 Production_companies are that we can work with it : ", "\n",
      production_companies_count_class_D.head(10))
diagram_production_companies_D = production_companies_count_class_D.head(20).plot.barh(fontsize=8)
# Set a title
diagram_production_companies_D.set(title='Top  production companies class D')
# x-label and y-label
diagram_production_companies_D.set_xlabel('Number of Movies')
diagram_production_companies_D.set_ylabel('List of cast')
# Show the plot
plt.show()
print("=" * 80)
# -------------------------------------
print("the Best Move IN this Class (D)")
print(tmdb_data_class_D.loc[tmdb_data_class_D["profit"].idxmax()])
print("=" * 80)
# -------------------------------------
print("the Worst Move IN this Class (D)")
print(tmdb_data_class_D.loc[tmdb_data_class_D["profit"].idxmin()])
print("=" * 80)
#####################################################################################################################
# if you want to make C class move
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Make C class move<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
tmdb_data_class_C = tmdb_data[tmdb_data["Class"] == "C"]
# -------------------------------------
print("The average budget of the movie will be :", tmdb_data_class_C["budget"].mean())
print("=" * 80)
print("The average revenue of the movie will be  :", tmdb_data_class_C["revenue"].mean())
print("=" * 80)
print("The average profit of the movie will be :", tmdb_data_class_C["profit"].mean())
print("=" * 80)
print("The average runtime of the movie will be :", tmdb_data_class_C["runtime"].mean())
print("=" * 80)
# -------------------------------------
genres_count_class_C = pd.Series(tmdb_data_class_C['genres'].str.cat(sep='|').split('|')).value_counts(ascending=False)
print("the Top 10 Genres are : ", "\n", genres_count_class_C.head(10))
print("=" * 80)
diagram_genres_C = genres_count_class_C.plot.bar(fontsize=8)
# Set a title
diagram_genres_C.set(title='Top Genres class_C')
# x-label and y-label
diagram_genres_C.set_xlabel('Type of genres')
diagram_genres_C.set_ylabel('Number of Movies')
# Show the plot
plt.show()
# -------------------------------------
cast_count_class_C = pd.Series(tmdb_data_class_C['cast'].str.cat(sep='|').split('|')).value_counts(ascending=False)
print("the Top 10 Cast are that we can work with it : ", "\n", cast_count_class_C.head(10))
diagram_cast_C = cast_count_class_C.head(20).plot.barh(fontsize=8)
# Set a title
diagram_cast_C.set(title='Top Cast class C')
# x-label and y-label
diagram_cast_C.set_xlabel('Number of Movies')
diagram_cast_C.set_ylabel('List of cast')
# Show the plot
plt.show()
print("=" * 80)
# -------------------------------------
production_companies_count_class_C = pd.Series(
    tmdb_data_class_C['production_companies'].str.cat(sep='|').split('|')).value_counts(ascending=False)
print("the Top 10 Production_companies are that we can work with it : ", "\n",
      production_companies_count_class_C.head(10))
diagram_production_companies_C = production_companies_count_class_C.head(20).plot.barh(fontsize=8)
# Set a title
diagram_production_companies_C.set(title='Top  production companies class C')
# x-label and y-label
diagram_production_companies_C.set_xlabel('Number of Movies')
diagram_production_companies_C.set_ylabel('List of cast')
# Show the plot
plt.show()
print("=" * 80)
# -------------------------------------
print("the Best Move IN this Class (C)")
print(tmdb_data_class_C.loc[tmdb_data_class_C["profit"].idxmax()])
print("=" * 80)
# -------------------------------------
print("the Worst Move IN this Class (C)")
print(tmdb_data_class_C.loc[tmdb_data_class_C["profit"].idxmin()])
print("=" * 80)
#####################################################################################################################
# if you want to make B class move
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Make B class move<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
tmdb_data_class_B = tmdb_data[tmdb_data["Class"] == "B"]
# -------------------------------------
print("The average budget of the movie will be :", tmdb_data_class_B["budget"].mean())
print("=" * 80)
print("The average revenue of the movie will be  :", tmdb_data_class_B["revenue"].mean())
print("=" * 80)
print("The average profit of the movie will be :", tmdb_data_class_B["profit"].mean())
print("=" * 80)
print("The average runtime of the movie will be :", tmdb_data_class_B["runtime"].mean())
print("=" * 80)
genres_count_class_B = pd.Series(tmdb_data_class_B['genres'].str.cat(sep='|').split('|')).value_counts(ascending=False)
print("the Top 10 Genres are : ", "\n", genres_count_class_B.head(10))
diagram_genres_B = genres_count_class_B.plot.bar(fontsize=8)
# Set a title
diagram_genres_B.set(title='Top Genres Class_B')
# x-label and y-label
diagram_genres_B.set_xlabel('Type of genres')
diagram_genres_B.set_ylabel('Number of Movies')
# Show the plot
plt.show()
# -------------------------------------
print("=" * 80)
cast_count_class_B = pd.Series(tmdb_data_class_B['cast'].str.cat(sep='|').split('|')).value_counts(ascending=False)
print("the 10 Top Cast are that we can work with it : ", "\n", cast_count_class_B.head(10))
diagram_cast_B = cast_count_class_B.head(20).plot.barh(fontsize=8)
# Set a title
diagram_cast_B.set(title='Top Cast class B')
# x-label and y-label
diagram_cast_B.set_xlabel('Number of Movies')
diagram_cast_B.set_ylabel('List of cast')
# Show the plot
plt.show()
print("=" * 80)
# -------------------------------------
production_companies_count_class_B = pd.Series(
    tmdb_data_class_B['production_companies'].str.cat(sep='|').split('|')).value_counts(ascending=False)
print("the Top 10 Production_companies are that we can work with it : ", "\n",
      production_companies_count_class_B.head(10))
diagram_production_companies_B = production_companies_count_class_B.head(20).plot.barh(fontsize=8)
# Set a title
diagram_production_companies_B.set(title='Top  production companies class B')
# x-label and y-label
diagram_production_companies_B.set_xlabel('Number of Movies')
diagram_production_companies_B.set_ylabel('List of cast')
# Show the plot
plt.show()
print("=" * 80)
# -------------------------------------
print("the Best Move IN this Class (B)")
print(tmdb_data_class_B.loc[tmdb_data_class_B["profit"].idxmax()])
print("=" * 80)
# -------------------------------------
print("the Worst Move IN this Class (B)")
print(tmdb_data_class_B.loc[tmdb_data_class_B["profit"].idxmin()])
print("=" * 80)
#####################################################################################################################
# if you want to make A class move
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Make A class move<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
tmdb_data_class_A = tmdb_data[tmdb_data["Class"] == "A"]
# -------------------------------------
print("The average budget of the movie will be :", tmdb_data_class_A["budget"].mean())
print("=" * 80)
print("The average revenue of the movie will be  :", tmdb_data_class_A["revenue"].mean())
print("=" * 80)
print("The average profit of the movie will be :", tmdb_data_class_A["profit"].mean())
print("=" * 80)
print("The average runtime of the movie will be :", tmdb_data_class_A["runtime"].mean())
print("=" * 80)
# -------------------------------------
genres_count_class_A = pd.Series(tmdb_data_class_A['genres'].str.cat(sep='|').split('|')).value_counts(ascending=False)
print("the Top 10 Genres are : ", "\n", genres_count_class_A.head(10))
print("=" * 80)
diagram_genres_A = genres_count_class_A.plot.bar(fontsize=8)
# Set a title
diagram_genres_A.set(title='Top Genres Class_A')
# x-label and y-label
diagram_genres_A.set_xlabel('Type of genres')
diagram_genres_A.set_ylabel('Number of Movies')
# Show the plot
plt.show()
# -------------------------------------
cast_count_class_A = pd.Series(tmdb_data_class_A['cast'].str.cat(sep='|').split('|')).value_counts(ascending=False)
print("the Top 10 Cast are that we can work with it : ", "\n", cast_count_class_A.head(10))
diagram_cast_A = cast_count_class_A.head(20).plot.barh(fontsize=8)
# Set a title
diagram_cast_A.set(title='Top Cast class A')
# x-label and y-label
diagram_cast_A.set_xlabel('Number of Movies')
diagram_cast_A.set_ylabel('List of cast')
# Show the plot
plt.show()
print("=" * 80)
# -------------------------------------
production_companies_count_class_A = pd.Series(
    tmdb_data_class_A['production_companies'].str.cat(sep='|').split('|')).value_counts(ascending=False)
print("the Top 10 Production_companies are that we can work with it : ", "\n",
      production_companies_count_class_A.head(10))
diagram_production_companies_A = production_companies_count_class_A.head(20).plot.barh(fontsize=8)
# Set a title
diagram_production_companies_A.set(title='Top  production companies class A')
# x-label and y-label
diagram_production_companies_A.set_xlabel('Number of Movies')
diagram_production_companies_A.set_ylabel('List of cast')
# Show the plot
plt.show()
print("=" * 80)
# -------------------------------------
print("the Best Move IN this Class (A)")
print(tmdb_data_class_A.loc[tmdb_data_class_A["profit"].idxmax()])
print("=" * 80)
print("the Worst Move IN this Class (A)")
print(tmdb_data_class_A.loc[tmdb_data_class_A["profit"].idxmin()])
print("=" * 80)
#####################################################################################################################
# if you want to make AA class move
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Make AA class move <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
tmdb_data_class_AA = tmdb_data[tmdb_data["Class"] == "AA"]
# -------------------------------------
print("The average budget of the movie will be :", tmdb_data_class_AA["budget"].mean())
print("=" * 80)
print("The average revenue of the movie will be  :", tmdb_data_class_AA["revenue"].mean())
print("=" * 80)
print("The average profit of the movie will be :", tmdb_data_class_AA["profit"].mean())
print("=" * 80)
print("The average runtime of the movie will be :", tmdb_data_class_AA["runtime"].mean())
print("=" * 80)
# ------------------------------------
genres_count_class_AA = pd.Series(tmdb_data_class_AA['genres'].str.cat(sep='|').split('|')).value_counts(
    ascending=False)
print("the Top 10 Genres are : ", "\n", genres_count_class_AA.head(10))
print("=" * 80)
diagram_genres_AA = genres_count_class_AA.plot.bar(fontsize=8)
# Set a title
diagram_genres_AA.set(title='Top Genres Class_AA')
# x-label and y-label
diagram_genres_AA.set_xlabel('Type of genres')
diagram_genres_AA.set_ylabel('Number of Movies')
# Show the plot
plt.show()
# -------------------------------------
cast_count_class_AA = pd.Series(tmdb_data_class_AA['cast'].str.cat(sep='|').split('|')).value_counts(ascending=False)
print("the Top 10 Cast are that we can work with it : ", "\n", cast_count_class_AA.head(10))
diagram_cast_AA = cast_count_class_AA.head(20).plot.barh(fontsize=8)
# Set a title
diagram_cast_AA.set(title='Top Cast class AA')
# x-label and y-label
diagram_cast_AA.set_xlabel('Number of Movies')
diagram_cast_AA.set_ylabel('List of cast')
# Show the plot
plt.show()
print("=" * 80)
# -------------------------------------
production_companies_count_class_AA = pd.Series(
    tmdb_data_class_AA['production_companies'].str.cat(sep='|').split('|')).value_counts(ascending=False)
print("the Top 10 Production_companies are that we can work with it : ", "\n",
      production_companies_count_class_AA.head(10))
diagram_production_companies_AA = production_companies_count_class_AA.head(20).plot.barh(fontsize=8)
# Set a title
diagram_production_companies_AA.set(title='Top  production companies class AA')
# x-label and y-label
diagram_production_companies_AA.set_xlabel('Number of Movies')
diagram_production_companies_AA.set_ylabel('List of cast')
# Show the plot
plt.show()
print("=" * 80)
# -------------------------------------
print("the Best Move IN this Class (AA)")
print(tmdb_data_class_AA.loc[tmdb_data_class_AA["profit"].idxmax()])
print("=" * 80)
print("the Worst Move IN this Class (AA)")
print(tmdb_data_class_AA.loc[tmdb_data_class_AA["profit"].idxmin()])
print("=" * 80)
#-------------------------------------
#####################################################################################################################
#####################################################################################################################
#The_End =)









