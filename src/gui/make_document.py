
import docx
import json

def make_document_from_json(
        json_file_path = "../../protocols/protocols_1/protocols.json",
        doc_save_path  = "../../documents/protocols_1.docx",
        meta_data      = {}
):
    
    doc = docx.Document()

    ############# FIRST PAGE #############
    main_heading_name   = "MSTS_Software_Protocols_1"
    document_name       = "MSRS_SOFT001A_01"
    revision            = "3.0"

    ## TODO revision hsitory

    prepared_by_name            = "name_1"
    prepared_by_designation     = "name_1_designation"
    prepared_by_date            = "01-01-2023"

    reviewed_by_name            = "reviewer_name"
    reviewed_by_designation     = "reviewer_designation"
    reviewed_by_data            = "01-01-2023"

    approved_by_name            = "approver_name"
    approved_by_designation     = "approver_designation"
    approved_by_date            = "01-01-2023"


    ############# SECOND PAGE #############
    purpose                     = "This document provides the test procedure\
                                    to verify protocols_1"
    scope                       = "This record applies to software requirement\
                                    implemented in protocols_1"
    testing_method              = "Tests are designed with inputs from software\
                                    requirements and use cases. The tests will be\
                                    executed at the system levels."
    tools_and_equipments_text   = "The required test equipment may vary for each\
                                    test case."
    
    list_of_hardware_equipments = [
        "hardware equipment 1",
        "hardware equipment 2"
    ]

    list_of_software_tools      = [
        "software tool 1",
        "software tool 2"
    ]


    safety_precautions_list     = [
        "safety precation 1",
        "safety precation 2",
        "safety precation 3"
    ]

    tester_identification       = {
        "tester_name"   : "name_1",
        "date"          : "01-01-2023"
    }

    ins












    doc.save(doc_save_path)

    return None


def main():
    make_document_from_json()

if __name__ == '__main__':
    main()