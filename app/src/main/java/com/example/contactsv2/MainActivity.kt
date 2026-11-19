package com.example.contactsv2

import android.app.Activity
import android.content.Intent
import android.os.Bundle
import android.widget.Toast
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AppCompatActivity
import com.example.contactsv2.databinding.ActivityMainBinding

/**
 * Activité principale affichant la ListView personnalisée de contacts.
 * Ouvre DetailActivity par Intent explicite et actualise la liste au retour du résultat.
 */
class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private lateinit var adapter: ContactAdapter

    val contacts = mutableListOf(
        Contact(1, "Dupont", "Claire", "06 12 34 56 78", "claire.dupont@example.com"),
        Contact(2, "Martin", "Thomas", "07 23 45 67 89", "thomas.martin@example.com"),
        Contact(3, "Bernard", "Sophie", "06 98 76 54 32", "sophie.bernard@example.com"),
        Contact(4, "Petit", "Lucas", "07 11 22 33 44", "lucas.petit@example.com"),
        Contact(5, "Moreau", "Julien", "06 55 44 33 22", "julien.moreau@example.com")
    )

    // Gestion moderne du retour de résultat d'activité
    private val detailActivityLauncher = registerForActivityResult(
        ActivityResultContracts.StartActivityForResult()
    ) { result ->
        if (result.resultCode == Activity.RESULT_OK) {
            val data = result.data
            @Suppress("DEPRECATION")
            val contactModifie = data?.getSerializableExtra(DetailActivity.EXTRA_CONTACT) as? Contact
            val position = data?.getIntExtra(DetailActivity.EXTRA_POSITION, -1) ?: -1

            if (contactModifie != null && position in contacts.indices) {
                contacts[position] = contactModifie
                adapter.notifyDataSetChanged()
                Toast.makeText(this, R.string.msg_contact_modifie, Toast.LENGTH_SHORT).show()
            }
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        adapter = ContactAdapter(this, contacts)
        binding.lvContacts.adapter = adapter

        // Clic sur un contact : ouverture de DetailActivity via Intent explicite
        binding.lvContacts.setOnItemClickListener { _, _, position, _ ->
            val contact = contacts[position]
            val intent = Intent(this, DetailActivity::class.java).apply {
                putExtra(DetailActivity.EXTRA_CONTACT, contact)
                putExtra(DetailActivity.EXTRA_POSITION, position)
            }
            detailActivityLauncher.launch(intent)
        }
    }
}
