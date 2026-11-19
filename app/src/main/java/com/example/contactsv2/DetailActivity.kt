package com.example.contactsv2

import android.app.Activity
import android.content.Intent
import android.graphics.Bitmap
import android.net.Uri
import android.os.Bundle
import android.widget.Toast
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AppCompatActivity
import com.example.contactsv2.databinding.ActivityDetailBinding

/**
 * Activité affichant le détail d'un contact et permettant sa modification.
 * Intègre les Intents explicites (retour de résultat) et implicites (Appel, E-mail, Galerie, Caméra).
 */
class DetailActivity : AppCompatActivity() {

    private lateinit var binding: ActivityDetailBinding
    private var contactActuel: Contact? = null
    private var positionContact: Int = -1
    private var photoSelectionneeUri: String? = null

    // Contrat pour choisir une photo depuis la galerie
    private val selectPictureLauncher = registerForActivityResult(
        ActivityResultContracts.GetContent()
    ) { uri: Uri? ->
        uri?.let {
            photoSelectionneeUri = it.toString()
            binding.ivDetailAvatar.setImageURI(it)
        }
    }

    // Contrat pour prendre une photo avec l'appareil photo
    private val takePictureLauncher = registerForActivityResult(
        ActivityResultContracts.TakePicturePreview()
    ) { bitmap: Bitmap? ->
        bitmap?.let {
            binding.ivDetailAvatar.setImageBitmap(it)
            // Stockage de la référence
            photoSelectionneeUri = "captured_bitmap"
        }
    }

    companion object {
        const val EXTRA_CONTACT = "extra_contact"
        const val EXTRA_POSITION = "extra_position"
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityDetailBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // Récupération des données transmises par l'Intent explicite
        @Suppress("DEPRECATION")
        contactActuel = intent.getSerializableExtra(EXTRA_CONTACT) as? Contact
        positionContact = intent.getIntExtra(EXTRA_POSITION, -1)

        // Pré-remplissage des champs
        contactActuel?.let { c ->
            binding.etNom.setText(c.nom)
            binding.etPrenom.setText(c.prenom)
            binding.etTelephone.setText(c.telephone)
            binding.etEmail.setText(c.email)
            photoSelectionneeUri = c.photoUri

            if (!c.photoUri.isNullOrEmpty()) {
                try {
                    binding.ivDetailAvatar.setImageURI(Uri.parse(c.photoUri))
                } catch (e: Exception) {
                    binding.ivDetailAvatar.setImageResource(R.drawable.ic_person)
                }
            }
        }

        // Action Retour
        binding.btnRetour.setOnClickListener {
            setResult(Activity.RESULT_CANCELED)
            finish()
        }

        // Action Annuler
        binding.btnAnnuler.setOnClickListener {
            setResult(Activity.RESULT_CANCELED)
            finish()
        }

        // Intent implicite : Composer un numéro de téléphone
        binding.btnAppeler.setOnClickListener {
            val tel = binding.etTelephone.text?.toString()?.trim().orEmpty()
            if (tel.isNotEmpty()) {
                val intentAppel = Intent(Intent.ACTION_DIAL, Uri.parse("tel:$tel"))
                try {
                    startActivity(intentAppel)
                } catch (e: Exception) {
                    Toast.makeText(this, R.string.msg_app_non_disponible, Toast.LENGTH_SHORT).show()
                }
            } else {
                binding.etTelephone.error = "Numéro vide"
            }
        }

        // Intent implicite : Envoyer un e-mail
        binding.btnEmail.setOnClickListener {
            val mail = binding.etEmail.text?.toString()?.trim().orEmpty()
            if (mail.isNotEmpty()) {
                val intentMail = Intent(Intent.ACTION_SENDTO).apply {
                    data = Uri.parse("mailto:$mail")
                }
                try {
                    startActivity(intentMail)
                } catch (e: Exception) {
                    Toast.makeText(this, R.string.msg_app_non_disponible, Toast.LENGTH_SHORT).show()
                }
            } else {
                binding.etEmail.error = "Adresse vide"
            }
        }

        // Choisir une photo dans la galerie
        binding.btnChoisirPhoto.setOnClickListener {
            selectPictureLauncher.launch("image/*")
        }

        // Prendre une photo avec la caméra
        binding.btnPrendrePhoto.setOnClickListener {
            try {
                takePictureLauncher.launch(null)
            } catch (e: Exception) {
                Toast.makeText(this, "Caméra non disponible", Toast.LENGTH_SHORT).show()
            }
        }

        // Action Enregistrer : renvoie les données à MainActivity
        binding.btnEnregistrer.setOnClickListener {
            enregistrerModifications()
        }
    }

    private fun enregistrerModifications() {
        val nom = binding.etNom.text?.toString()?.trim().orEmpty()
        val prenom = binding.etPrenom.text?.toString()?.trim().orEmpty()
        val tel = binding.etTelephone.text?.toString()?.trim().orEmpty()
        val email = binding.etEmail.text?.toString()?.trim().orEmpty()

        if (nom.isEmpty() || prenom.isEmpty() || tel.isEmpty()) {
            Toast.makeText(this, R.string.erreur_champs_obligatoires, Toast.LENGTH_LONG).show()
            return
        }

        val contactModifie = Contact(
            id = contactActuel?.id ?: 0,
            nom = nom,
            prenom = prenom,
            telephone = tel,
            email = email,
            photoUri = photoSelectionneeUri
        )

        val resultIntent = Intent().apply {
            putExtra(EXTRA_CONTACT, contactModifie)
            putExtra(EXTRA_POSITION, positionContact)
        }

        setResult(Activity.RESULT_OK, resultIntent)
        finish()
    }
}
