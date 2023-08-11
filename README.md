## STEPS PER ESEGUIRE
Per eseguire lo script si deve eseguire i seguenti passi:

1. Aprire il prompt dei commandi e posizionarsi nella cartella 'assets'. Scaricare il model eseguendo le due istruzioni:
   * git lfs install
   * git clone https://huggingface.co/95gas/DONUT-model

3. Posizionarsi nel root della cartella ed eseguire il commando
   * pip install .
5. Eseguire lo script
   * python main.py

Per testare il programma, le immagini devono essere inserite nella cartella 'test'. Successivamente, il programma leggerà tutte le immagini contenute nella cartella e le processerà ritornando a schermo i risultati. 


## RUN ON COLAB
Nella root della repository è disponibile il notebook 'Run DONUT on Colab.ipynb' che riporta in maniera guidata i passi spiegati sopra se si desidera eseguire il programma sulla piattaforma Colab. 
