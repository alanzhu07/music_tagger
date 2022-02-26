import predict

tagger = predict.Predictor()
tagger.setup()
result = tagger.predict("data/chaos.mp3", "Harmonic CNN", "")
print(result)