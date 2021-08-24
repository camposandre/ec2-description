# ec2-description

Lista propriedades de uma EC2 AWS e gera um arquivo csv com essas informações.

Integrantes: André Rodrigues / Alexandre / Anderson / Roberto (Bob) / Mauro

----------------------------------------------------------------------------

VERSÕES

Version_Lambda_S3Bucket >> código para executar em AWS Lambda, gera o resultado em um arquivo csv para um S3 Bucket.

Version_Local_HardDrive >> código para executar localmente (notebook), gera o resultado em um arquivo csv dentro do seu hard drive local.

Version_Local_S3Bucket >> código para executar localmente (notebook), gera o resultado em um arquivo csv para um S3 Bucket.

-----------------------------------------------------------------------------

INSTRUÇÕES

Version_Lambda_S3Bucket >>

Alterar o código e inserir o nome do bucket onde o csv deve ser gerado.
A role da lambda deve ter permissões para ler as EC2 e gravar no bucket de destino.

Version_Local_HardDrive >>

Importar os módulos boto3 e csv.

Version_Local_S3Bucket >> 

Importar os módulos boto3 e csv.
Alterar o código e inserir o nome do bucket onde o csv deve ser gerado
A conta que vai executar o código deve ter direitos de escrita no bucket de destino.
