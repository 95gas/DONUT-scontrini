## STEPS PER ESEGUIRE
Per eseguire lo script si deve eseguire i seguenti passi:

1. Aprire il prompt dei commandi e posizionarsi nella cartella 'assets'. Scaricare il modello eseguendo le seguenti due istruzioni:
   * git lfs install
   * git clone https://huggingface.co/95gas/DONUT-model

2. Posizionarsi nella root della cartella ed eseguire il commando
   * pip install .
  
3. Inserire le immagini degli scontrini nella cartella 'test'
     
3. Eseguire lo script. Il programma leggerà tutte le immagini contenute nella cartella 'test' e le processerà una ad una ritornando a schermo i risultati. 
   * python main.py




## RUN ON COLAB
Nella root della repository è disponibile il notebook 'Run DONUT on Colab.ipynb' che riporta in maniera guidata i passi spiegati sopra se si desidera eseguire il programma sulla piattaforma Colab. 
