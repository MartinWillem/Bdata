Eigen Datamet correlatie getallen en geen treshold:
Opgeslagen in:
Categorisch
NB_Cat_NT = niet binominaal, categorisch, no threshold

Clasificaties zonder aanpassingen in instellingen:
NB_Cat_NT_1.0: Cross Validation + Decision tree + performance(classafication)						| classification_error: 57.19% +/- 0.64% (mikro: 57.19%)	| kappa: 0.006 +/- 0.017 (mikro: 0.006)	| logistic_loss: 0.578 +/- 0.003 (mikro: 0.578)
NB_Cat_NT_2.0: Cross Validation + Knn + performance(classafication)							| classification_error: 25.17% +/- 2.59% (mikro: 25.17%)	| kappa: 0.662 +/- 0.035 (mikro: 0.662)	| logistic_loss: 0.409 +/- 0.010 (mikro: 0.409)
NB_Cat_NT_3.0: Cross Validation + Naive Bayas + performance(classafication)						| classification_error: 28.18% +/- 5.25% (mikro: 28.19%)	| kappa: 0.645 +/- 0.061 (mikro: 0.644)	| logistic_loss: 0.422 +/- 0.016 (mikro: 0.422)
NB_Cat_NT_4.0: Splitt + Decision tree + performance(classafication)							| classification_error: 55.60%					| kappa: 0.049				| logistic_loss: 0.571
NB_Cat_NT_5.0: splitt + Knn + performance(classafication)								| classification_error: 27.80%					| kappa: 0.630				| logistic_loss: 0.419
NB_Cat_NT_6.0: Splitt + Naive Bayas + performance(classafication)							| classification_error: 25.87%					| kappa: 0.672				| logistic_loss: 0.419
NB_Cat_NT_7.0: Bootstrapping + Decision tree + performance(classafication)						| classification_error: 53.70% +/- 4.01% (mikro: 53.70%)	| kappa: 0.066 +/- 0.097 (mikro: 0.069)	| logistic_loss: 0.568 +/- 0.020 (mikro: 0.568)
NB_Cat_NT_8.0: Bootstrapping + Knn + performance(classafication)							| classification_error: 26.87% +/- 1.72% (mikro: 26.90%)	| kappa: 0.634 +/- 0.022 (mikro: 0.634)	| logistic_loss: 0.415 +/- 0.007 (mikro: 0.415)
NB_Cat_NT_9.0: Bootstrapping + Naive Bayas + performance(classafication)						| classification_error: 28.13% +/- 2.10% (mikro: 28.15%)	| kappa: 0.639 +/- 0.024 (mikro: 0.639)	| logistic_loss: 0.421 +/- 0.007 (mikro: 0.421)

Clasificaties met aanpassingen in de training:
NB_Cat_NT_10.0: Cross Validation + Decision tree(Accuracy + No prunning) + performance(classafication)			| classification_error: 23.78% +/- 3.57% (mikro: 23.78%)	| kappa: 0.676 +/- 0.051 (mikro: 0.676)	| logistic_loss: 0.417 +/- 0.012 (mikro: 0.417)
NB_Cat_NT_11.0: Cross Validation + Knn(5-nn) + performance(classafication)						| classification_error: 26.21% +/- 2.59% (mikro: 26.22%)	| kappa: 0.634 +/- 0.037 (mikro: 0.634)	| logistic_loss: 0.432 +/- 0.008 (mikro: 0.432)
NB_Cat_NT_12.0: Cross Validation + Naive Bayas(No Laplace corractie) + performance(classafication)			| classification_error: 100.00% +/- 0.00% (mikro: 100.00%)	| kappa: -0.000 +/- 0.000(mikro: -0.001)| logistic_loss: 0.693 +/- 0.000 (mikro: 0.693)
NB_Cat_NT_13.0: Splitt + Decision tree(Accuracy + No prunning) + performance(classafication)				| classification_error: 31.66%					| kappa: 0.576				| logistic_loss: 0.442
NB_Cat_NT_14.0: Splitt + Knn(5-nn) + performance(classafication)							| classification_error: 27.03%					| kappa: 0.622				| logistic_loss: 0.436
NB_Cat_NT_15.0: Splitt + Naive Bayas(No Laplace corractie) + performance(classafication)				| classification_error: 100.00%					| kappa: -0.000				| logistic_loss: 0.693
NB_Cat_NT_16.0: Bootstrapping + Decision tree(Accuracy + No prunning) + performance(classafication)			| classification_error: 28.41% +/- 1.75% (mikro: 28.41%)	| kappa: 0.605 +/- 0.027 (mikro: 0.605)	| logistic_loss: 0.433 +/- 0.007 (mikro: 0.433)
NB_Cat_NT_17.0: Bootstrapping + Knn(5-nn) + performance(classafication)							| classification_error: 27.55% +/- 1.30% (mikro: 27.54%)	| kappa: 0.617 +/- 0.019 (mikro: 0.618)	| logistic_loss: 0.430 +/- 0.005 (mikro: 0.430)
NB_Cat_NT_18.0: Bootstrapping + Naive Bayas(No Laplace corractie) + performance(classafication)				| classification_error: 99.93%					| kappa: 0.001				| logistic_loss: unknown

Clasificaties met aanpassingen in de Validation:
/NB_Cat_NT_19.0: Cross Validation(LOO) + Decision tree + performance(classafication)					| classification_error: 57.42% +/- 49.45% (mikro: 57.42%)	| kappa: 0.000				| logistic_loss: 0.580 +/- 0.073 (mikro: 0.580)
/NB_Cat_NT_20.0: Cross Validation(LOO) + Knn + performance(classafication)						| classification_error: 25.29% +/- 43.47% (mikro: 25.29%)	| kappa: 0.660				| logistic_loss: 0.409 +/- 0.165 (mikro: 0.409)
/NB_Cat_NT_21.0: Cross Validation(LOO) + Naive Bayas + performance(classafication)					| classification_error: 26.68% +/- 44.23% (mikro: 26.68%)	| kappa: 0.662				| logistic_loss: 0.416 +/- 0.152 (mikro: 0.416)
NB_Cat_NT_22.0: Splitt(split.2, stratified) + Decision tree + performance(classafication)				| classification_error: 56.07%					| kappa: 0.049				| logistic_loss: 0.574
NB_Cat_NT_23.0: splitt(split.2, stratified) + Knn + performance(classafication)						| classification_error: 22.54%					| kappa: 0.695				| logistic_loss: 0.399
NB_Cat_NT_24.0: Splitt(split.2, stratified) + Naive Bayas + performance(classafication)					| classification_error: 24.86%					| kappa: 0.680				| logistic_loss: 0.409
NB_Cat_NT_25.0: Bootstrapping(N20) + Decision tree + performance(classafication)					| classification_error: 54.76% +/- 4.05% (mikro: 54.76%)	| kappa: 0.056 +/- 0.077 (mikro: 0.058)	| logistic_loss: 0.569 +/- 0.015 (mikro: 0.569) 
NB_Cat_NT_26.0: Bootstrapping(N20) + Knn + performance(classafication)							| classification_error: 28.28% +/- 2.59% (mikro: 28.28%)	| kappa: 0.617 +/- 0.031 (mikro: 0.617)	| logistic_loss: 0.421 +/- 0.010 (mikro: 0.421)
NB_Cat_NT_27.0: Bootstrapping(N20) + Naive Bayas + performance(classafication)						| classification_error: 28.53% +/- 2.30% (mikro: 28.53%)	| kappa: 0.636 +/- 0.025 (mikro: 0.636)	| logistic_loss: 0.422 +/- 0.008 (mikro: 0.422)

Clasificaties met aanpassingen in de training en in de Validation:
NB_Cat_NT_28.0: Cross Validation(LOO) + Decision tree(Accuracy + No prunning) + performance(classafication)		| classification_error: 25.75% +/- 43.73% (mikro: 25.75%)	| kappa: 0.649				| logistic_loss: 0.424 +/- 0.156 (mikro: 0.424)
NB_Cat_NT_29.0: Cross Validation(LOO) + Knn(5-nn) + performance(classafication)						| classification_error: 25.52% +/- 43.60% (mikro: 25.52%)	| kappa: 0.645				| logistic_loss: 0.430 +/- 0.132 (mikro: 0.430)
NB_Cat_NT_30.0: Cross Validation(LOO) + Naive Bayas(No Laplace corractie) + normal performance(classafication)		| classification_error: 100.00% +/- 0.00% (mikro: 100.00%)	| kappa: 0.000 +/- 0.000 (mikro: -0.001)| logistic_loss: 0.693 +/- 0.000 (mikro: 0.693)
NB_Cat_NT_31.0: Splitt(split.2, stratified) + Decision tree(Accuracy + No prunning) + performance(classafication)	| classification_error: 24.86%					| kappa: 0.657				| logistic_loss: 0.424
NB_Cat_NT_32.0: Splitt(split.2, stratified) + Knn(5-nn) + performance(classafication)					| classification_error: 23.70%					| kappa: 0.673				| logistic_loss: 0.426
NB_Cat_NT_33.0: Splitt(split.2, stratified) + Naive Bayas(No Laplace corractie) + performance(classafication)		| classification_error: 100.00%					| kappa: 0.000				| logistic_loss: 0.693
NB_Cat_NT_34.0: Bootstrapping(N20) + Decision tree(Accuracy + No prunning) + performance(classafication)		| classification_error: 28.46% +/- 2.35% (mikro: 28.45%)	| kappa: 0.608 +/- 0.033 (mikro: 0.609)	| logistic_loss: 0.432 +/- 0.008 (mikro: 0.432)
NB_Cat_NT_35.0: Bootstrapping(N20) + Knn(5-nn) + performance(classafication)						| classification_error: 28.72% +/- 2.40% (mikro: 28.71%)	| kappa: 0.603 +/- 0.029 (mikro: 0.603)	| logistic_loss: 0.432 +/- 0.007 (mikro: 0.432)
NB_Cat_NT_36.0: Bootstrapping(N20) + Naive Bayas(No Laplace corractie) + performance(classafication)			| classification_error: 99.95%					| kappa: -0.000				| logistic_loss: unknown


