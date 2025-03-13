import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Substitua pelo seu token do Telegram BotFather
TOKEN = "7797954824:AAEB4kw-vtmBmgWR502k51ymXBCJ9knzx1A"
bot = telebot.TeleBot(TOKEN)

# Dicionário com os protocolos organizados por categoria e subcategoria
protocolos = {
    "📞Atendimento": {
        "💲Financeiro": [
            {"titulo": "Boleto Não Liquidado", "descricao": "Casos em que o pagamento já foi efetuado, mas não foi registrado no sistema. Inclui análise do comprovante de pagamento, comunicação com bancos e regularização do status financeiro do cliente\n\n- *Status:* Andamento\n- *Verificar comprovante de pagamento*\n- *Encaminhar ao Faturamento*", "imagem": "https://i.ibb.co/j47594x/BOLETO-N-O-LIQUIDADO.png"},
            {"titulo": "Carnê", "descricao": "Opção para clientes que desejam seus boletos em formato de carnê, o que reduz a procura por segunda via de modo geral.\n\n- *Status:* Andamento\n*-Encaminhar ao Faturamento*", "imagem": "https://via.placeholder.com/300"},
            {"titulo": "Contestação de Fatura", "descricao": "Atendimento para revisar cobranças consideradas indevidas ou inconsistentes. O cliente pode questionar valores adicionais, erros de cálculo ou serviços não contratados, com suporte detalhado e investigação do caso.\n\n- *Status:* Andamento\n*-Encaminhar ao Faturamento*", "imagem": "https://i.ibb.co/vqp7TXS/CONTESTACAO-DE-FATURA.png"},
            {"titulo": "Desbloqueio", "descricao": "Atendimento realizado para reativar os serviços suspensos por atraso de pagamento ou outros motivos. Geralmente inclui a regularização financeira e a reconexão do serviço de forma automática ou manual.\n\n- *Status:* Andamento\n*-Encaminhar ao Faturamento*", "imagem": "https://i.ibb.co/TWZVC3h/DESBLOQUEIO.png"},
            {"titulo": "Download APP", "descricao": "Protocolo gerado para auxílio e download do APP do cliente GBSNET.\n\n- *Status:* Encerramento", "imagem": "https://via.placeholder.com/300"},
            {"titulo": "Informe de Pagamento", "descricao": "Atendimento voltado para anexos de pagamentos já realizados. Inclui dados como valores pagos, datas de vencimento, métodos de pagamento aceitos e eventuais descontos aplicáveis.\n\n- *Status:* Andamento\n*-Anexar o Comprovante!*\n*-Encaminhar ao Faturamento*", "imagem": "https://i.ibb.co/3YjL5h6/INFORME-DE-PAG.png"},
            {"titulo": "Negociação de Débitos", "descricao": "Processo de renegociação de valores em atraso, permitindo parcelamentos ou abatimentos para regularização do contrato. É uma solução que evita a suspensão do serviço e mantém o cliente ativo na base.\n\n- *Status:* Andamento\n*-Elaborar a Proposta!*\n*-Encaminhar para Cobrança*", "imagem": "https://i.ibb.co/2k3nsNc/NEGOCIACAO.png"},
            {"titulo": "Pagamento (Liquidação)", "descricao": "Processo destinado a registrar e confirmar o pagamento de faturas pendentes. O cliente pode apresentar comprovantes de pagamento ou solicitar auxílio para localizar transações não identificadas, garantindo a continuidade do serviço.\n\n- *Status:* Andamento\n*-Anexar o Comprovante!*\n*-Encaminhar ao Faturamento*", "imagem": "https://i.ibb.co/KDKg23Y/PAGAMENTO-LIQ.png"},
            {"titulo": "Segunda via de Fatura", "descricao": "Solicitação para emitir uma nova cópia de uma fatura mensal. O documento pode ser enviado por e-mail, WhatsApp ou disponibilizado via portal e aplicativo da GBSNET.\n\n- *Status:* Encerramento\n*-Validar os dados!*", "imagem": "https://i.ibb.co/2W27BT3/SEGUNDA-VIA.png"},
            {"titulo": "Segunda via de NF", "descricao": "Solicitação para emitir, reimprimir ou esclarecer dúvidas sobre a nota fiscal do serviço contratado. Inclui orientações sobre como acessar o documento e detalhes sobre impostos cobrados.\n\n- *Status:* Andamento\n*-Encaminhar ao Odisseu / Financeiro*", "imagem": "https://i.ibb.co/M9Nv5HC/NOTA-FISCAL.png"},
            {"titulo": "Solicitação de Descontos", "descricao": "O cliente pode pedir redução nos valores cobrados, relacionado a rede, sendo possível solicitar por Sem Conexão e Internet Lenta. Essa solicitação passa por análise técnica pelo Service Suport e aplicação posterior pelo Faturamento (Prazo 30 dias).\n\n- *Status:* Andamento\n*-Validar o intervalo de datas!*\n*-Encaminhar ao Service Suport*", "imagem": "https://i.ibb.co/T4JRZCG/DESCONTO.png"},

        ],
        "📑Contrato": [
            {"titulo": "Reativação", "descricao": "Protocolo realizado para clientes que estão com o contrato suspenso ou cancelados e desejam reativar para usar novamente a conexão da empresa.\n\n- *Status:* Andamento\n*-Encaminhar ao Faturamento*", "imagem": "https://via.placeholder.com/300"},
            {"titulo": "Suspensão", "descricao": "Opção para suspender temporariamente o contrato sem cancelá-lo definitivamente. Geralmente oferecida para clientes que não utilizarão o serviço por um período, mas pretendem mantê-lo ativo posteriormente.\n\n- *Status:* Andamento\n*-Encaminhar ao Faturamento*", "imagem": "https://i.ibb.co/P1nx6PT/SUSPENSAO.png"},
            {"titulo": "Troca de Titularidade", "descricao": "Transferência do contrato para outro titular, seja por motivos pessoais ou financeiros. Envolve atualização dos dados cadastrais e assinatura de um novo contrato por conta do novo titular. Documentos necessários: Nome Completo, Telefone, CPF, Identidade, Email e também é necessário realizar a verificação SPC do cpf. \n\n- *Status:* Andamento\n*-Encaminhar ao Customer Sucess*", "imagem": "https://i.ibb.co/ZcxXgyY/TITULARIDADE.png"},
            {"titulo": "Troca de Vencimento", "descricao": "Solicitação para mudar a data de vencimento das faturas, ajustando ao cronograma financeiro do cliente. Inclui análise de prazos e procedimentos internos para realizar a alteração. É necessário realizar a simulação e apresentar ao cliente antes de prosseguir com o protocolo.\n\n- *Status:* Andamento\n*-Anexar o aceite e o cálculo*\n*-Encaminhar ao Faturamento*", "imagem": "https://i.ibb.co/s18R3JD/ALT-DE-VENCIMENTO.png"}
        ],
        "💬Informações": [
            {"titulo": "Informações", "descricao": "Serviço destinado a fornecer detalhes sobre os planos e serviços disponíveis, características técnicas, benefícios e condições contratuais. Essa solicitação é comum entre novos clientes ou usuários que precisam esclarecer dúvidas gerais sobre a GBSNET, como cobertura, velocidades disponíveis ou regras de uso.\n\n- *Status:* Andamento", "imagem": "https://i.ibb.co/VV8Jw05/INFORMACOES.png"},
        ], # type: ignore

        "💭Ouvidoria": [
            {"titulo": "Reclamação", "descricao": "Os operadores devem registrar todos os chamados no sistema com detalhes.\n\n- *Status:* Andamento\n*-Encaminhar para Customer Sucess*", "imagem": "https://via.placeholder.com/300"},
            {"titulo": "Solicitação", "descricao": "Os operadores devem registrar todos os chamados no sistema com detalhes.\n\n- *Status:* Andamento\n*-Encaminhar para Customer Sucess*", "imagem": "https://via.placeholder.com/300"},
            {"titulo": "Sugestão", "descricao": "Utilizar linguagem cordial e seguir o script padrão.\n\n- *Status:* Andamento\n*-Encaminhar para Customer Sucess*", "imagem": "https://via.placeholder.com/300"}
        ], # type: ignore
    },
    "💱Venda": {
        "Serviços": [
            {"titulo": "Mudança de Ambiente", "descricao": "Transferência de equipamentos dentro do mesmo imóvel, como mover o roteador para outro cômodo. Pode exigir ajustes técnicos para garantir a qualidade do sinal.\n\n- *Status:* Agendamento\n*-Encaminhar para Equipe Técnica de Campo*", "imagem": "https://i.ibb.co/524FNrH/MUDANCA-DE-AMBIENTE.png"},
            {"titulo": "Mudança de Endereço", "descricao": "Pedido para transferir o serviço para um novo endereço. Envolve análise de viabilidade técnica e agendamento de visita técnica para instalação no novo local.\n\n- *Status:* Agendamento\n*-Encaminhar para Equipe Técnica de Campo*", "imagem": "https://i.ibb.co/b1sYW9f/MUDANCA-DE-ENDERECO.png"},
            {"titulo": "Renovação Contratual", "descricao": "Processo de renovação de contratos que estão próximos do vencimento. Pode incluir atualização de valores, condições e adesão a novos planos com SVA’s ou promoções disponíveis.", "imagem": "https://i.ibb.co/qdhjF8C/RENOVA-O.png"},
            {"titulo": "Outros Serviços", "descricao": "Lista de promoções em vigor para novos e antigos clientes.\n\n- *Status:* Andamento\n*-Encaminhar para Faturamento*", "imagem": "https://via.placeholder.com/300"}
        ]
    },
    "📲Suporte Técnico": {
        "🚔O.S": [
            {"titulo": "Auxílio de Configurações", "descricao": "Protocolo realizados pela central de atendimento para um técnico configurar os equipamentos do cliente em sua residência. Inclui ajustes em roteadores, atualizações e testes de conexão.\n\n- *Status:* Agendamento\n*-Encaminhar para Equipe Técnica de Campo*", "imagem": "https://i.ibb.co/ynJ19mN/AUX-CONFIG-OS.png"},
            {"titulo": "Sem Conexão", "descricao": "Atendimentos em que a falta de conexão exige a abertura de uma ordem de serviço para envio de um técnico. Inclui diagnóstico detalhado e ações corretivas no local.\n\n- *Status:* Agendamento\n*-Encaminhar para Equipe Técnica de Campo*", "imagem": "https://i.ibb.co/syy7M2D/SEM-CONEXAO-OS.png"},
            {"titulo": "Internet Lenta", "descricao": "Solicitação de visita técnica para resolver problemas de lentidão na conexão, após falhas nas tentativas de solução remota.\n\n- *Status:* Agendamento\n*-Encaminhar para Equipe Técnica de Campo*", "imagem": "https://i.ibb.co/5TdVwNS/INTERNET-LENTA-OS.png"}
        ]
    },
    "❌Pedido de Cancelamento": {
        "Retenção": [
            {"titulo": "Solicitação de Cancelamento", "descricao": "Pedido para encerrar o contrato de prestação de serviço. O atendimento busca entender os motivos e, se possível, oferece alternativas como upgrades ou descontos para evitar a saída do cliente.\n\n- *Status:* Andamento\n*-Encaminhar para Customer Sucess*", "imagem": "https://i.ibb.co/VJgk7gZ/CANCELAMENTO.png"},
        ]
    }
}

# Função para criar o menu principal
def menu_principal():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for categoria in protocolos.keys():
        markup.add(KeyboardButton(categoria))
    markup.add(KeyboardButton("🔄 Reiniciar"))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Olá! Escolha uma categoria para consultar um protocolo:", reply_markup=menu_principal())

@bot.message_handler(func=lambda message: message.text in protocolos.keys())
def selecionar_subcategoria(message):
    categoria = message.text
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for subcategoria in protocolos[categoria].keys():
        markup.add(KeyboardButton(subcategoria))
    markup.add(KeyboardButton("🔄 Voltar"))
    bot.send_message(message.chat.id, f"Selecione uma subcategoria de {categoria}:", reply_markup=markup)

@bot.message_handler(func=lambda message: any(message.text in protocolos[categoria] for categoria in protocolos))
def selecionar_protocolo(message):
    for categoria, subcategorias in protocolos.items():
        if message.text in subcategorias:
            subcategoria = message.text
            markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            for protocolo in subcategorias[subcategoria]:
                markup.add(KeyboardButton(protocolo["titulo"]))
            markup.add(KeyboardButton("🔄 Voltar"))
            bot.send_message(message.chat.id, f"Selecione um protocolo em {subcategoria}:", reply_markup=markup)
            return

@bot.message_handler(func=lambda message: any(message.text in [p["titulo"] for sub in protocolos[c].values() for p in sub] for c in protocolos))
def enviar_protocolo(message):
    for categoria, subcategorias in protocolos.items():
        for subcategoria, lista_protocolos in subcategorias.items():
            for protocolo in lista_protocolos:
                if message.text == protocolo["titulo"]:
                    bot.send_photo(message.chat.id, protocolo["imagem"], caption=f"📌 *{protocolo['titulo']}*\n\n{protocolo['descricao']}", parse_mode='Markdown')
                    return

@bot.message_handler(func=lambda message: message.text == "🔄 Voltar")
def voltar(message):
    bot.send_message(message.chat.id, "Escolha uma categoria:", reply_markup=menu_principal())

@bot.message_handler(func=lambda message: message.text == "🔄 Reiniciar")
def reiniciar(message):
    start(message)

bot.polling()