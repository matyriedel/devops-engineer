resource "aws_instance"{
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = "Desafio11_MRIEDEL"
  }

  key_name = "Mriedel_Desafio11_Key.pem"
}