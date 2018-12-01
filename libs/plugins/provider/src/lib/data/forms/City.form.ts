import { FormControl, Validators, FormGroup } from '@angular/forms';

import { AbstractForm } from '@webdjangular/core/data-forms';
import { ScaffoldFieldConfig } from '@webdjangular/core/interfaces';
import { StreetForm } from './Street.form';
import { RangeForm } from './Range.form';

export class CityForm extends AbstractForm {

  public listingTableSettings = {
    columns: {
      id: {
        title: 'ID',
        type: 'number',
      },
      name: {
        title: 'Name',
        type: 'string',
      },
      short_name: {
        title: 'Short Name',
        type: 'string',
      },
    },
  };

  formFields = {
    pk: {
      type: FormControl,
    },
    name: {
      type: FormControl,
      validators: [Validators.required]
    },
    short_name: {
      type: FormControl,
      validators: [Validators.required]
    },
    streets: {
      type: FormGroup,
      formClass: StreetForm,
    },
    zips: {
      type: FormGroup,
      formClass: RangeForm,
    },
    created: {
      type: FormControl,
    },
    updated: {
      type: FormControl,
    },
  }

  scaffoldFields: ScaffoldFieldConfig[] = [
    {
      type: 'input',
      label: 'Name',
      name: 'name',
      placeholder: 'Enter City Name',
    },
    {
      type: 'input',
      label: 'Short Name',
      name: 'short_name',
      placeholder: 'Entery City Short Name (NY)',
    },
  ]
}