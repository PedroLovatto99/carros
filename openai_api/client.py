from openai import OpenAI


client = OpenAI(
    api_key='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'
)


def get_car_ai_bio(model, brand, year):
    message = ''''
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo.
    Descreva especificações técnicas desse modelo de carro.
    '''
    message = message.format(brand, model, year)
    response = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': message
            }
        ],
        max_tokens=1000,
        model='gpt-3.5-turbo',
    )

    return response.choices[0].message.content