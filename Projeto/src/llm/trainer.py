import torch 
import argparse
import logging 
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
from dataset import load_dataset

#Criar uma classe que vai agrupar as funções essenciais para criação do modelo LLM 
class ModelConstruct:
    #Vai iniciar o modelo 
    def _init_(self, num_layers, num_heads, vocab_size, d_model):
        self.modelName = DS_TCC
        #variavel para o numero de camadas 
        self.num_layers = 
        #
        self.num_heads = 
        self.vocab_size = 
        self.d_model = 
        self.d_ff =
        self.dropout_rate =

    def 
    def
    def 
    def 