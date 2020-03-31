python3 LogisticRegresstion.py
[INFO]: Training model
[Parallel(n_jobs=1)]: Using backend SequentialBackend with 1 concurrent workers.
RUNNING THE L-BFGS-B CODE

           * * *

Machine precision = 2.220D-16
 N =        20405     M =           10
 This problem is unconstrained.

At X0         0 variables are exactly at the bounds

At iterate    0    f=  1.69100D+03    |proj g|=  3.99213D+04

At iterate   50    f=  2.43058D+02    |proj g|=  2.61216D+03

At iterate  100    f=  8.72164D+00    |proj g|=  2.79325D+02

At iterate  150    f=  1.43923D-01    |proj g|=  7.96125D-01

At iterate  200    f=  8.43356D-02    |proj g|=  2.52285D-01

At iterate  250    f=  6.05486D-02    |proj g|=  1.04079D-01

At iterate  300    f=  4.86977D-02    |proj g|=  7.10260D-02

At iterate  350    f=  4.26374D-02    |proj g|=  6.34888D-02

At iterate  400    f=  3.95456D-02    |proj g|=  5.55994D-02

At iterate  450    f=  3.74243D-02    |proj g|=  1.79069D-02

At iterate  500    f=  3.64503D-02    |proj g|=  1.52659D-02

At iterate  550    f=  3.57931D-02    |proj g|=  2.11215D-02

At iterate  600    f=  3.53938D-02    |proj g|=  2.01876D-02

At iterate  650    f=  3.51111D-02    |proj g|=  6.91971D-03

At iterate  700    f=  3.49396D-02    |proj g|=  7.90816D-03

At iterate  750    f=  3.48572D-02    |proj g|=  8.13764D-03

At iterate  800    f=  3.48016D-02    |proj g|=  3.53875D-03

At iterate  850    f=  3.47701D-02    |proj g|=  2.05071D-03

At iterate  900    f=  3.47502D-02    |proj g|=  4.65163D-03

At iterate  950    f=  3.47421D-02    |proj g|=  1.32942D-03

           * * *

Tit   = total number of iterations
Tnf   = total number of function evaluations
Tnint = total number of segments explored during Cauchy searches
Skip  = number of BFGS updates skipped
Nact  = number of active bounds at final generalized Cauchy point
Projg = norm of the final projected gradient
F     = final function value

           * * *

   N    Tit     Tnf  Tnint  Skip  Nact     Projg        F
20405    971   1046      1     0     0   7.499D-04   3.474D-02
  F =  3.47401590847464248E-002

CONVERGENCE: NORM_OF_PROJECTED_GRADIENT_<=_PGTOL
[Parallel(n_jobs=1)]: Done   1 out of   1 | elapsed:   13.8s finished
[INFO]: Accurancy on validation data: 0.8556701030927835
                   precision    recall  f1-score   support

     Ariel Sharon       0.67      0.62      0.64        13
     Colin Powell       0.80      0.88      0.84        60
  Donald Rumsfeld       0.63      0.81      0.71        27
    George W Bush       0.94      0.89      0.91       146
Gerhard Schroeder       0.85      0.88      0.86        25
      Hugo Chavez       0.83      0.67      0.74        15
       Tony Blair       0.84      0.75      0.79        36

         accuracy                           0.84       322
        macro avg       0.79      0.79      0.79       322
     weighted avg       0.85      0.84      0.85       322