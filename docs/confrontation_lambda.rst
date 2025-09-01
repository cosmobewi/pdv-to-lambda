.. _confrontation_lambda:

===========================================
Confrontation aux cadres existants pour Λ
===========================================

Objectif
--------

Situer notre hypothèse « conversion p dV → Λ » par rapport aux cadres usuels,
en partant des équations de fond et du schéma d’échange minimal.

Rappels (GR) et schéma d’échange
--------------------------------

.. math::
   :name: eq:friedmann

   H^2=\frac{8\pi G}{3}\rho_{\rm tot} - \frac{k}{a^2}, 
   \qquad \rho_{\rm tot}=\rho_r+\rho_m+\rho_\Lambda.

Évolution avec **échange rayonnement ↔ vide** (matière conservée au fond) :

.. math::
   :name: eq:exchange

   \begin{aligned}
   \dot\rho_r + 4H\rho_r &= -\,Q,\\
   \dot\rho_m + 3H\rho_m &= 0,\\
   \dot\rho_\Lambda     &= +\,Q, \qquad 
   Q(a)=\eta(a)\,H\,\rho_r.
   \end{aligned}

- **Paramétrisation lisse recommandée** (fenêtre tardive, pondération comobile) :
  :math:`\eta(a)=\eta_0\,a^3\,\frac{1+\tanh\!\big(\frac{a-a_\star}{\Delta}\big)}{2}`.
- **Conséquence intégrée (ordre de grandeur)** : 
  :math:`\Omega_{\Lambda0}\simeq \eta_0\,\Omega_{r0}\,z_\star`
  (voir démo dans la section précédente).

Où se place notre scénario ?
---------------------------

- **Λ constant** : :math:`Q=0`. Notre modèle le retrouve pour :math:`\eta\to 0`.
- **QFT/EFT** : lecture micro de :math:`\rho_\Lambda` (pas de prédiction robuste de sa valeur).
- **Running Vacuum (RVM)** : :math:`\rho_\Lambda(H)` ⇒ échange effectif ; 
  branche où :math:`Q\propto H\rho_r` proche de notre ansatz (ici spécifique au rayonnement).
- **IDE / viscosité effective** : cas particulier d’interaction sombre ; 
  nous ne couplons **pas** la matière non relativiste au fond.
- **Quintessence** : pas de champ scalaire additionnel ici ; l’évolution apparente
  de Λ vient du terme :math:`Q`, pas d’un potentiel :math:`V(\phi)`.
- **Unimodulaire / Sequestering** : mécanismes géométriques d’annulation globale ;
  approche conceptuellement différente de notre source locale :math:`Q(a)`.

Signatures attendues (observables)
----------------------------------

- **Corrélation** : :math:`\Omega_{\Lambda0}`–:math:`N_{\rm eff}` via :math:`\Omega_{r0}` 
  (dépend de l’hypothèse sur :math:`\eta(a)` et :math:`z_\star`).
- **Léger “phantom dip”** de :math:`w_\Lambda^{\rm eff}(z)=-1-\eta(a)\rho_r/(3\rho_\Lambda)` 
  près de :math:`z_\star` (amplitude :math:`\sim 10^{-4}\eta_0` aujourd’hui).
- **Courbure douce de :math:`H(z)`** testable par BAO radiales / chronomètres cosmiques.
- Effets faibles mais corrélés sur **ISW tardif**, **RSD** et :math:`\sigma_8` (à quantifier).

.. tip::
   Pour la confrontation : scanner :math:`(a_\star,\Delta,\eta_0)` sous contrainte BBN/CMB 
   (préférer une fenêtre **post-recombinaison** ou très douce avant), puis ajuster SN/BAO/H(z), 
   RSD et lensing (ISW).