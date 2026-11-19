package com.example.contactsv2

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotNull
import org.junit.Test

/**
 * Tests unitaires validant le modèle de données Contact et les opérations de mise à jour.
 */
class ContactModelTest {

    @Test
    fun testCreationEtModificationContact() {
        val contact = Contact(
            id = 1,
            nom = "Dupont",
            prenom = "Claire",
            telephone = "06 12 34 56 78",
            email = "claire.dupont@example.com"
        )

        assertNotNull(contact)
        assertEquals("Dupont", contact.nom)
        assertEquals("Claire", contact.prenom)

        // Modification
        contact.nom = "Durand"
        contact.telephone = "06 99 88 77 66"

        assertEquals("Durand", contact.nom)
        assertEquals("06 99 88 77 66", contact.telephone)
    }

    @Test
    fun testValidationChampsObligatoires() {
        val nom = "Dupont"
        val prenom = "Claire"
        val tel = ""

        val estValide = nom.isNotBlank() && prenom.isNotBlank() && tel.isNotBlank()
        assertEquals(false, estValide)
    }
}
