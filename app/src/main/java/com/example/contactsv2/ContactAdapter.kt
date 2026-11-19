package com.example.contactsv2

import android.content.Context
import android.net.Uri
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ArrayAdapter
import android.widget.ImageView
import android.widget.TextView

/**
 * Adaptateur personnalisé pour afficher la liste de contacts avec leur avatar, nom, prénom et téléphone.
 */
class ContactAdapter(
    context: Context,
    private val contacts: List<Contact>
) : ArrayAdapter<Contact>(context, 0, contacts) {

    override fun getView(position: Int, convertView: View?, parent: ViewGroup): View {
        val view = convertView ?: LayoutInflater.from(context).inflate(R.layout.item_contact, parent, false)
        val contact = getItem(position) ?: return view

        val tvNomComplet = view.findViewById<TextView>(R.id.tvNomComplet)
        val tvTelephone = view.findViewById<TextView>(R.id.tvTelephone)
        val ivAvatar = view.findViewById<ImageView>(R.id.ivAvatar)

        tvNomComplet.text = "${contact.nom} ${contact.prenom}"
        tvTelephone.text = contact.telephone

        if (!contact.photoUri.isNullOrEmpty()) {
            try {
                ivAvatar.setImageURI(Uri.parse(contact.photoUri))
            } catch (e: Exception) {
                ivAvatar.setImageResource(R.drawable.ic_person)
            }
        } else {
            ivAvatar.setImageResource(R.drawable.ic_person)
        }

        return view
    }
}
