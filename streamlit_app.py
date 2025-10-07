#import streamlit as st
#import pandas as pd
#import numpy as np


#titanic = pd.read_csv('https://huggingface.co/datasets/ankislyakov/titanic/resolve/main/titanic_train.csv', index_col='PassengerId')

#survived_by_sex = titanic.groupby('Sex')['Survived'].value_counts(normalize=True).unstack() * 100
#count_by_sex = titanic.groupby('Sex')['Survived'].value_counts().unstack()

#st.write("Количество и процент выживших и погибших по полу:")
#st.write(count_by_sex)

#st.write("\nПроцент:")
#st.dataframe(survived_by_sex)

import streamlit as st
import pandas as pd
import numpy as np


titanic = pd.read_csv('https://huggingface.co/datasets/ankislyakov/titanic/resolve/main/titanic_train.csv', index_col='PassengerId')

st.title("Анализ данных Титаника")

survival_choice = st.radio(
    "Выберите тип статистики:",
    ["Показать выживших", "Показать погибших"],
    horizontal=True
)

display_choice = st.radio(
    "Выберите способ отображения:",
    ["Показать проценты", "Показать только количество"],
    horizontal=True
)

if survival_choice == "Показать выживших":
    survived_data = titanic[titanic['Survived'] == 1]
    title = "Статистика выживших"
else:
    survived_data = titanic[titanic['Survived'] == 0]
    title = "Статистика погибших"

men_count = len(survived_data[survived_data['Sex'] == 'male'])
women_count = len(survived_data[survived_data['Sex'] == 'female'])
total_count = len(survived_data)

if total_count > 0:
    men_percentage = (men_count / total_count) * 100
    women_percentage = (women_count / total_count) * 100
else:
    men_percentage = women_percentage = 0

st.subheader(title)

if display_choice == "Показать проценты":
    results_df = pd.DataFrame({
        'Пол': ['Мужчины', 'Женщины', 'Всего'],
        'Процент': [f'{men_percentage:.1f}%', f'{women_percentage:.1f}%', '100%']
    })
    
else:
    results_df = pd.DataFrame({
        'Пол': ['Мужчины', 'Женщины', 'Всего'],
        'Количество': [men_count, women_count, total_count]
    })

st.table(results_df)

st.info(f"Проанализированы данные {total_count} пассажиров")