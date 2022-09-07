# Python program to generate a WordCloud based on a given list of words/phrases and frequencies

# importing modules
from wordcloud import WordCloud
import pandas as pd

# read the spreadsheet file into a pandas dataframe
df = pd.read_excel(r"words.xlsx")
print("number of words: " + str(df.shape[0])) # print the number of words going into the word cloud

# re-format the word and frequency pairs into a dictionary
d = dict(zip(df['word'], df['frequency']))

# generate the word cloud with a list of custom attributes
# for documentation, please refer to: 
# https://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html
wordcloud = WordCloud(
    font_path="C:\Windows\Fonts\Oswald-VariableFont_wght.TTF", # choose your own font here
    width=1920,
    height=600,
    prefer_horizontal=1, # 1 means I want all words to be horizontal 
    scale=1, 
    relative_scaling=0.4, # gives a good balance between the biggest and smallest font sizes
    min_font_size=12, 
    max_font_size=36, 
    font_step=1,
    max_words=200, 
    repeat=False,
    include_numbers=False,
    min_word_length=0, 
    background_color=None, mode="RGBA", # gives transparent background
    colormap="copper", 
    color_func=None
)
wordcloud.generate_from_frequencies(d)
# save the file
wordcloud.to_file("wordcloud.png")
