import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox


import random


class Bienvenue:
    def __init__(self, root):
        self.root = root
        self.root.title("Bienvenue")


        image_path = r'C:\Users\hp\Downloads\Design sans titre.png'
        self.image = PhotoImage(file=image_path)


        self.label_image = tk.Label(self.root, image=self.image)
        self.label_image.pack()

        self.button_entree_jeux = tk.Button(self.root, text="Entrer dans l'espace des jeux", command=self.entrer_jeux,
                                            font=('Helvetica', 20), bg='#3498db', fg='white')
        self.button_entree_jeux.pack(pady=20)

    def entrer_jeux(self):
        self.root.destroy()
        root = tk.Tk()
        interface = JeuxInterface(root)
        root.mainloop()


class JeuxInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeux avec Interface Graphique")

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        image_path_1 = r'C:\Users\hp\Downloads\Design sans titre (1).png'
        self.image_1 = self.charger_et_redimensionner_image(image_path_1)
        # Afficher l'image dans une étiquette
        self.label_image_1 = tk.Label(self.frame, image=self.image_1)
        self.label_image_1.grid(row=0, column=0, padx=10, pady=10)

        self.button_tic_tac_toe = tk.Button(self.frame, text="Tic-Tac-Toe", command=self.jouer_tic_tac_toe,
                                            font=('Helvetica', 16), bg='#3498db', fg='white')
        self.button_tic_tac_toe.grid(row=1, column=0, padx=10, pady=10)

        image_path_2 = r'C:\Users\hp\Downloads\Design sans titre (3).png'
        self.image_2 = self.charger_et_redimensionner_image(image_path_2)
        # Afficher l'image dans une étiquette
        self.label_image_2 = tk.Label(self.frame, image=self.image_2)
        self.label_image_2.grid(row=0, column=1, padx=10, pady=10)

        self.button_pendu = tk.Button(self.frame, text="Le Pendu", command=self.jouer_pendu, font=('Helvetica', 16),
                                      bg='#e74c3c', fg='white')
        self.button_pendu.grid(row=1, column=1, padx=10, pady=10)

        image_path_3 = r'C:\Users\hp\Downloads\Design sans titre (2).png'
        self.image_3 = self.charger_et_redimensionner_image(image_path_3)
        # Afficher l'image dans une étiquette
        self.label_image_3 = tk.Label(self.frame, image=self.image_3)
        self.label_image_3.grid(row=0, column=2, padx=10, pady=10)

        self.button_devine_nombre = tk.Button(self.frame, text="Devine le Nombre", command=self.jouer_devine_nombre,
                                              font=('Helvetica', 16), bg='#2ecc71', fg='white')
        self.button_devine_nombre.grid(row=1, column=2, padx=10, pady=10)

        image_path_5 = r'C:\Users\hp\Downloads\Design sans titre (4).png'
        self.image_5 = self.charger_et_redimensionner_image(image_path_5)
        self.label_image_5 = tk.Label(self.frame, image=self.image_5)
        self.label_image_5.grid(row=0, column=4, padx=10, pady=10)
        # Afficher l'image dans une étiquette
        self.button_puissance_4 = tk.Button(self.frame, text="Puissance 4", command=self.jouer_puissance4,
                                            font=('Helvetica', 16), bg='#f39c12', fg='white')
        self.button_puissance_4.grid(row=1, column=4, padx=10, pady=10, sticky='nsew')

        image_path_6 = r'C:\Users\hp\Downloads\Design sans titre (5).png'
        self.image_6 = self.charger_et_redimensionner_image(image_path_6)
        self.label_image_6 = tk.Label(self.frame, image=self.image_6)
        self.label_image_6.grid(row=0, column=5, padx=10, pady=10)
        # Add a new row for the Quiz button
        self.button_quiz_math = tk.Button(self.frame, text="Quiz Mathématique", command=self.jouer_quiz_math,
                                          font=('Helvetica', 16), bg='#e67e22', fg='white')
        self.button_quiz_math.grid(row=1, column=5, padx=10, pady=10)

    def charger_et_redimensionner_image(self, path, height=None):
        try:
            pil_image = tk.PhotoImage(file=path)
            tk_image = pil_image.subsample(2, 2)  # Adjust the subsample factor as needed
            return tk_image
        except Exception as e:
            print(f"Error loading image: {e}")
            return None

    def jouer_quiz_math(self):
        QuizMath()

    def jouer_puissance4(self):
        Puissance4()

    def jouer_tic_tac_toe(self):
        TicTacToe()

    def jouer_pendu(self):
        Pendu()

    def jouer_devine_nombre(self):
        DevineNombre()

class QuizMath:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Quiz Mathématique")

        self.questions = []
        self.generer_questions()

        self.question_actuelle = 0
        self.score = 0

        self.frame = tk.Frame(self.root, padx=20, pady=20)
        self.frame.pack()

        tk.Label(self.frame, text="Quiz Mathématique", font=('Helvetica', 24, 'bold')).grid(row=0, column=0,
                                                                                            columnspan=2, pady=10)

        self.label_question = tk.Label(self.frame, text="", font=('Helvetica', 16))
        self.label_question.grid(row=1, column=0, columnspan=2, pady=20)

        self.entree_reponse = tk.Entry(self.frame, font=('Helvetica', 16))
        self.entree_reponse.grid(row=2, column=0, columnspan=2, pady=20)

        tk.Button(self.frame, text="Soumettre", command=self.verifier_reponse, font=('Helvetica', 16)).grid(row=3,
                                                                                                            column=0,
                                                                                                            columnspan=2,
                                                                                                            pady=10)

        self.label_score = tk.Label(self.frame, text=f"Score: {self.score}", font=('Helvetica', 16))
        self.label_score.grid(row=4, column=0, columnspan=2, pady=10)

        self.label_question_actuelle = tk.Label(self.frame, text="", font=('Helvetica', 16))
        self.label_question_actuelle.grid(row=5, column=0, columnspan=2, pady=10)

        self.afficher_question_suivante()

    def generer_questions(self):
        for _ in range(5):  # Vous pouvez ajuster le nombre de questions
            operande1 = random.randrange(1, 21)
            operande2 = random.randrange(1, 21)
            reponse = operande1 + operande2

            question_text = f"{operande1} + {operande2} ="

            self.questions.append({"question": question_text, "reponse": str(reponse)})

    def afficher_question_suivante(self):
        if self.question_actuelle < len(self.questions):
            question = self.questions[self.question_actuelle]["question"]

            self.label_question.config(text=question)
            self.label_question_actuelle.config(text=f"Question {self.question_actuelle + 1}")
            self.entree_reponse.delete(0, tk.END)
        else:
            messagebox.showinfo("Quiz Mathématique", f"Quiz terminé. Votre score est {self.score}.")
            self.root.destroy()

    def verifier_reponse(self):
        reponse_utilisateur = self.entree_reponse.get()
        reponse_correcte = self.questions[self.question_actuelle]["reponse"]

        if reponse_utilisateur == reponse_correcte:
            messagebox.showinfo("Quiz Mathématique", "Bonne réponse !")
            self.score += 1
        else:
            messagebox.showinfo("Quiz Mathématique", f"Mauvaise réponse. La réponse correcte est {reponse_correcte}.")

        self.question_actuelle += 1
        self.label_score.config(text=f"Score: {self.score}")
        self.afficher_question_suivante()

class TicTacToe:
        def __init__(self):
            self.root = tk.Tk()
            self.root.title("Tic-Tac-Toe")

            self.joueur_actif = "X"
            self.boutons = [[None, None, None], [None, None, None], [None, None, None]]

            for i in range(3):
                for j in range(3):
                    self.boutons[i][j] = tk.Button(self.root, text="", font=('Arial', 35), width=6, height=3,
                                                   command=lambda row=i, col=j: self.jouer(row, col), bg='moccasin',
                                                   activebackground='moccasin')
                    self.boutons[i][j].grid(row=i, column=j)

        def jouer(self, row, col):
            if self.boutons[row][col]["text"] == "" and not self.partie_terminee():
                self.boutons[row][col]["text"] = self.joueur_actif
                if self.partie_gagnee():
                    messagebox.showinfo("Tic-Tac-Toe", f"Le joueur {self.joueur_actif} a gagné !")
                    self.reinitialiser()
                elif self.partie_terminee():
                    messagebox.showinfo("Tic-Tac-Toe", "Match nul !")
                    self.reinitialiser()
                else:
                    self.joueur_actif = "O" if self.joueur_actif == "X" else "X"

        def partie_gagnee(self):
            for i in range(3):
                if self.boutons[i][0]["text"] == self.boutons[i][1]["text"] == self.boutons[i][2]["text"] != "":
                    return True
                if self.boutons[0][i]["text"] == self.boutons[1][i]["text"] == self.boutons[2][i]["text"] != "":
                    return True
            if self.boutons[0][0]["text"] == self.boutons[1][1]["text"] == self.boutons[2][2]["text"] != "":
                return True
            if self.boutons[0][2]["text"] == self.boutons[1][1]["text"] == self.boutons[2][0]["text"] != "":
                return True
            return False

        def partie_terminee(self):
            for i in range(3):
                for j in range(3):
                    if self.boutons[i][j]["text"] == "":
                        return False
            return True

        def reinitialiser(self):
            for i in range(3):
                for j in range(3):
                    self.boutons[i][j]["text"] = ""
            self.joueur_actif = "X"


class Pendu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Le Pendu")

        self.mots = ["python", "interface", "graphique", "jeu", "pendu", "programmation", "openai", "structure",
                     "quize"]
        self.mot_a_deviner = random.choice(self.mots)
        self.mot_affiche = ["_"] * len(self.mot_a_deviner)
        self.lettres_utilisees = []

        self.tentatives_restantes = 7

        tk.Label(self.root, text="Devine le mot:", font=('Helvetica', 16)).pack()

        self.label_mot_affiche = tk.Label(self.root, text=" ".join(self.mot_affiche), font=('Helvetica', 16),
                                          bg="moccasin")
        self.label_mot_affiche.pack()

        tk.Label(self.root, text="Lettres utilisées:", font=('Helvetica', 16)).pack()

        self.label_lettres_utilisees = tk.Label(self.root, text=", ".join(self.lettres_utilisees),
                                                font=('Helvetica', 16))
        self.label_lettres_utilisees.pack()

        tk.Label(self.root, text=f"Tentatives restantes: {self.tentatives_restantes}", font=('Helvetica', 16)).pack()

        self.entree_lettre = tk.Entry(self.root, font=('Helvetica', 16), bg="moccasin")
        self.entree_lettre.pack()

        tk.Button(self.root, text="Vérifier", command=self.verifier_lettre, font=('Helvetica', 16),
                  bg="moccasin").pack()

    def verifier_lettre(self):
        lettre = self.entree_lettre.get().lower()

        if lettre.isalpha() and len(lettre) == 1:
            if lettre in self.lettres_utilisees:
                messagebox.showinfo("Le Pendu", "Vous avez déjà utilisé cette lettre.")
            else:
                self.lettres_utilisees.append(lettre)
                self.label_lettres_utilisees.config(text=", ".join(self.lettres_utilisees))

                if lettre in self.mot_a_deviner:
                    for i in range(len(self.mot_a_deviner)):
                        if self.mot_a_deviner[i] == lettre:
                            self.mot_affiche[i] = lettre
                    self.label_mot_affiche.config(text=" ".join(self.mot_affiche))

                    if "_" not in self.mot_affiche:
                        messagebox.showinfo("Le Pendu", "Bravo, vous avez deviné le mot!")
                        self.root.destroy()
                else:
                    self.tentatives_restantes -= 1
                    tk.Label(self.root, text=f"Tentatives restantes: {self.tentatives_restantes}",
                             font=('Helvetica', 16), bg="moccasin").pack()

                    if self.tentatives_restantes == 0:
                        messagebox.showinfo("Le Pendu", f"Perdu ! Le mot était {self.mot_a_deviner}.")
                        self.root.destroy()
        else:
            messagebox.showinfo("Le Pendu", "Veuillez entrer une lettre valide.")


class DevineNombre:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Devine le Nombre")

        self.nombre_a_deviner = random.randint(1, 100)
        self.tentatives_restantes = 10

        tk.Label(self.root, text="Devinez le nombre entre 1 et 100:", font=('Helvetica', 16)).pack()

        self.entree_nombre = tk.Entry(self.root, font=('Helvetica', 16))
        self.entree_nombre.pack()

        tk.Button(self.root, text="Vérifier", command=self.verifier_nombre, font=('Helvetica', 16)).pack()

        tk.Label(self.root, text=f"Tentatives restantes: {self.tentatives_restantes}", font=('Helvetica', 16)).pack()

        tk.Button(self.root, text="Recommencer", command=self.recommencer, font=('Helvetica', 16)).pack()

    def verifier_nombre(self):
        try:
            nombre_propose = int(self.entree_nombre.get())
            if 1 <= nombre_propose <= 100:
                self.tentatives_restantes -= 1
                if nombre_propose == self.nombre_a_deviner:
                    messagebox.showinfo("Devine le Nombre",
                                        f"Félicitations ! Vous avez deviné le nombre {self.nombre_a_deviner}.")
                    self.recommencer()
                elif nombre_propose < self.nombre_a_deviner:
                    messagebox.showinfo("Devine le Nombre", "Essayez un nombre plus grand. Essayez à nouveau.")
                else:
                    messagebox.showinfo("Devine le Nombre", "Essayez un nombre plus petit. Essayez à nouveau.")

                if self.tentatives_restantes == 0:
                    messagebox.showinfo("Devine le Nombre",
                                        f"Désolé, vous avez épuisé toutes les tentatives. Le nombre était {self.nombre_a_deviner}.")
                    self.recommencer()

                tk.Label(self.root, text=f"Tentatives restantes: {self.tentatives_restantes}",
                         font=('Helvetica', 16)).pack()
            else:
                messagebox.showinfo("Devine le Nombre", "Veuillez entrer un nombre entre 1 et 100.")
        except ValueError:
            messagebox.showinfo("Devine le Nombre", "Veuillez entrer un nombre valide.")

    def recommencer(self):
        self.root.destroy()
        DevineNombre()


class Puissance4:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Puissance 4")

        self.joueur_actif = "Jaune"
        self.couleurs_joueurs = {"Jaune": "yellow", "Rouge": "red"}

        self.boutons = [[None] * 7 for _ in range(6)]

        for i in range(6):
            for j in range(7):
                self.boutons[i][j] = tk.Button(self.root, text="", width=5, height=2, bg="white",
                                               command=lambda col=j: self.jouer(col))
                self.boutons[i][j].grid(row=i, column=j)

    def jouer(self, col):
        for i in range(5, -1, -1):
            if self.boutons[i][col]["bg"] == "white":
                self.boutons[i][col]["bg"] = self.couleurs_joueurs[self.joueur_actif]
                if self.partie_gagnee(i, col):
                    messagebox.showinfo("Puissance 4", f"Le joueur {self.joueur_actif} a gagné !")
                    self.reinitialiser()
                elif self.partie_nulle():
                    messagebox.showinfo("Puissance 4", "Match nul !")
                    self.reinitialiser()
                else:
                    self.joueur_actif = "Rouge" if self.joueur_actif == "Jaune" else "Jaune"
                break

    def partie_gagnee(self, row, col):
        couleur = self.couleurs_joueurs[self.joueur_actif]

        # Vérification horizontale
        if col <= 3 and all(self.boutons[row][col + i]["bg"] == couleur for i in range(4)):
            return True

        # Vérification verticale
        if row <= 2 and all(self.boutons[row + i][col]["bg"] == couleur for i in range(4)):
            return True

        # Vérification diagonale (/)
        if row >= 3 and col <= 3 and all(
                0 <= row - i < 6 and 0 <= col + i < 7 and self.boutons[row - i][col + i]["bg"] == couleur for i in
                range(4)):
            return True

        # Vérification diagonale (\)
        if row <= 2 and col <= 3 and all(self.boutons[row + i][col + i]["bg"] == couleur for i in range(4)):
            return True

        return False

    def partie_nulle(self):
        return all(self.boutons[0][col]["bg"] != "white" for col in range(7))

    def reinitialiser(self):
        for i in range(6):
            for j in range(7):
                self.boutons[i][j]["bg"] = "white"
        self.joueur_actif = "Jaune"


if __name__ == "__main__":
    root = tk.Tk()
    bienvenue = Bienvenue(root)
    root.mainloop()
