Feature: Formulário de Contato

  Scenario: Enviar mensagem
     Given Entro na Página de contato do Instituto Joga Junto
      When Insiro meus dados
      And Envio a mensagem "Olá da turma de QA Avançado, Ilhabela Novembro 2024"
      Then Fecho o navegador