{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a3e95dad-ebd6-43d2-9846-91cb6fb24442",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.metrics import classification_report, accuracy_score\n",
    "\n",
    "# 1. Load your dataset (e.g., weatherAUS or custom data)\n",
    "# df = pd.read_csv('your_data.csv')\n",
    "\n",
    "# 2. Define features and target\n",
    "# X = df.drop(columns=['RainTomorrow'])\n",
    "# y = df['RainTomorrow']\n",
    "\n",
    "# 3. Train-test split\n",
    "# X_train, X_test, y_train, y_test = train_test_split(\n",
    "#     X, y, test_size=0.2, random_state=42, stratify=y\n",
    "# )\n",
    "\n",
    "# 4. Initialize models\n",
    "models = {\n",
    "    \"Random Forest\": RandomForestClassifier(random_state=42),\n",
    "    \"Logistic Regression\": LogisticRegression(max_iter=1000, random_state=42)\n",
    "}\n",
    "\n",
    "# 5. Train and evaluate\n",
    "for name, model in models.items():\n",
    "    print(f\"--- {name} ---\")\n",
    "    model.fit(X_train, y_train)\n",
    "    y_pred = model.predict(X_test)\n",
    "    \n",
    "    print(f\"Accuracy: {accuracy_score(y_test, y_pred):.2f}\\n\")\n",
    "    print(\"Classification Report:\")\n",
    "    print(classification_report(y_test, y_pred))\n",
    "    print(\"=\"*40)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
