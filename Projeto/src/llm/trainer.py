import torch 
import argparse
import logging 
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
from dataset import load_dataset

class SimpleCausaLlm(nn.Module):
    def __init__(self):
    def embedding(self):
    def decodificador(self):
    def causal_mask(self):
    def linear_layer(self):
    def dropout_rate(self):
    def num_heads(self):
    def num_layers(self):
    def batch_size(self):
    def num_epochs(self):
    def device(self):
    def learning_rate(self):
    def d_ff(self):
     
#Criar uma classe que vai agrupar as funções essenciais para criação do modelo LLM 00
class ModelConstruct(SimpleCausaLlm):
    # Vai iniciar o modelo  
    def __init__(self, modelname="DS_TCC", num_layers=12, num_heads=8, vocab_size=5000, 
                 d_model=512, d_ff=2048, dropout_rate=0.1, batch_size=128, num_epochs=10, 
                 learning_rate=5e-5, device="cpu"):
        self.modelName = modelname
        self.num_layers = num_layers
        self.num_heads = num_heads 
        self.vocab_size = vocab_size
        self.d_model = d_model
        self.d_ff = d_ff
        self.dropout_rate = dropout_rate
        self.learning_rate = learning_rate  
        self.batch_size = batch_size
        self.num_epochs = num_epochs
        self.device = device
        self.embedding = embed

    def create_model(self):

        model = SimpleCausaLlm(
        vocab_size=self.vocab_size,
        d_model=self.d_model,
        num_heads=self.num_heads,
        num_layers=self.num_layers,
        d_ff=self.d_ff,
        dropout_rate=self.dropout_rate
    )
    
    # 
    model.to(self.device)

    return model 
        
    def load_data(self):
    def train(self):
    def predict(self):
    def save_model(self):
    def load_trained_model(self):